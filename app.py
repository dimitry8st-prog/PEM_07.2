"""Flask-веб-интерфейс: чат и мультимодальная генерация изображений."""

import os
import threading
import time
import uuid
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_from_directory

from config import detect_provider
from pipeline import OUTPUTS_DIR, run_multimodal_pipeline
from providers import GigaChatProvider, ProxyAPIImageProvider, get_provider

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", os.urandom(24).hex())

tasks_status: dict[str, dict] = {}
tasks_lock = threading.Lock()


def _set_task(task_id: str, **fields) -> None:
    with tasks_lock:
        tasks_status.setdefault(task_id, {})
        tasks_status[task_id].update(fields)


def _process_chat_task(task_id: str, prompt: str) -> None:
    try:
        _set_task(task_id, status="processing", progress=10, message="Инициализация...")
        provider_name = detect_provider()
        provider = get_provider(provider_name)

        _set_task(
            task_id,
            progress=40,
            message=f"Отправка запроса ({provider_name})...",
        )
        response = provider.send_message(prompt)

        _set_task(
            task_id,
            status="completed",
            progress=100,
            message="Готово!",
            result={
                "mode": "chat",
                "provider": provider_name,
                "prompt": prompt,
                "response": response,
            },
        )
    except Exception as exc:
        _set_task(task_id, status="error", progress=0, message=f"Ошибка: {exc}")


def _process_image_task(task_id: str, prompt: str) -> None:
    try:
        _set_task(task_id, status="processing", progress=5, message="Запуск пайплайна...")

        def on_progress(progress: int, message: str) -> None:
            _set_task(task_id, status="processing", progress=progress, message=message)

        result = run_multimodal_pipeline(prompt, on_progress=on_progress)
        image_name = Path(result.image_path).name
        session_id = result.session_id

        _set_task(
            task_id,
            status="completed",
            progress=100,
            message="Готово!",
            result={
                "mode": "image",
                "prompt": result.original_prompt,
                "refined_prompt": result.refined_prompt,
                "image_url": f"/outputs/{session_id}/{image_name}",
                "session_id": session_id,
                "timings_sec": result.timings_sec,
                "total_sec": result.total_sec,
            },
        )
    except Exception as exc:
        _set_task(task_id, status="error", progress=0, message=f"Ошибка: {exc}")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()
    mode = (data.get("mode") or "image").strip().lower()

    if not prompt:
        return jsonify({"error": "Промпт не может быть пустым"}), 400

    if mode not in {"chat", "image"}:
        return jsonify({"error": "Режим должен быть chat или image"}), 400

    try:
        if mode == "chat":
            detect_provider()
        else:
            GigaChatProvider()
            ProxyAPIImageProvider()
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    task_id = f"task_{uuid.uuid4().hex[:12]}"
    _set_task(task_id, status="queued", progress=0, message="Задача в очереди...")

    target = _process_chat_task if mode == "chat" else _process_image_task
    thread = threading.Thread(target=target, args=(task_id, prompt), daemon=True)
    thread.start()

    return jsonify({"task_id": task_id})


@app.route("/api/status/<task_id>")
def api_status(task_id: str):
    with tasks_lock:
        task = tasks_status.get(task_id)

    if not task:
        return jsonify({"error": "Задача не найдена"}), 404

    return jsonify(task)


@app.route("/outputs/<session_id>/<filename>")
def serve_output(session_id: str, filename: str):
    directory = OUTPUTS_DIR / session_id
    if not directory.exists():
        return jsonify({"error": "Файл не найден"}), 404
    return send_from_directory(directory, filename)


if __name__ == "__main__":
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", "5000"))
    app.run(host=host, port=port, debug=False, threaded=True)
