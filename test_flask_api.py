#!/usr/bin/env python3
"""Интеграционный тест Flask API."""

import json
import sys
import time
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:5000"


def request_json(method: str, path: str, data: dict | None = None) -> tuple[int, dict]:
    body = None
    headers = {}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        f"{BASE}{path}",
        data=body,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode())


def wait_task(task_id: str, timeout: int = 180) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        code, data = request_json("GET", f"/api/status/{task_id}")
        if code != 200:
            raise RuntimeError(f"status {code}: {data}")
        if data.get("status") in {"completed", "error"}:
            return data
        time.sleep(1)
    raise TimeoutError(f"task {task_id} timed out")


def test_index() -> None:
    req = urllib.request.Request(f"{BASE}/")
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode()
    assert resp.status == 200
    assert "AI Генератор" in html
    print("OK index page")


def test_image_mode() -> None:
    code, data = request_json(
        "POST",
        "/api/generate",
        {"mode": "image", "prompt": "Красное яблоко на белом фоне"},
    )
    assert code == 200, data
    task = wait_task(data["task_id"], timeout=180)
    assert task["status"] == "completed", task
    assert "image_url" in task["result"]
    img_req = urllib.request.Request(f"{BASE}{task['result']['image_url']}")
    with urllib.request.urlopen(img_req, timeout=30) as resp:
        assert resp.status == 200
        assert resp.read(8)[:4] == b"\x89PNG"
    print("OK image mode:", task["result"]["image_url"])


def test_chat_mode() -> None:
    code, data = request_json(
        "POST",
        "/api/generate",
        {"mode": "chat", "prompt": "Привет! Ответь одним предложением."},
    )
    assert code == 200, data
    task = wait_task(data["task_id"], timeout=60)
    if task["status"] == "error" and "unsupported_country" in task.get("message", ""):
        print("SKIP chat mode: OpenAI region blocked (use GigaChat only)")
        return
    assert task["status"] == "completed", task
    assert task["result"]["response"]
    print("OK chat mode:", task["result"]["provider"])


def main() -> None:
    test_index()
    test_image_mode()
    test_chat_mode()
    print("\nAll tests passed")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
