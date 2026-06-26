#!/usr/bin/env python3
"""Генерация текстового PDF-отчёта по фактическим данным проекта PEM_07.2."""

import json
from pathlib import Path

from fpdf import FPDF

PROJECT = Path(__file__).parent
OUTPUT = PROJECT / "PEM_07_2_отчёт.pdf"
FONT = Path("C:/Windows/Fonts/segoeui.ttf")


def load_runs() -> list[dict]:
    runs = []
    for meta in sorted(PROJECT.glob("outputs/*/metadata.json")):
        data = json.loads(meta.read_text(encoding="utf-8"))
        runs.append(data)
    return runs


def build_report() -> None:
    runs = load_runs()
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.set_margins(14, 12, 14)
    pdf.add_font("Ru", "", str(FONT))

    w = pdf.w - pdf.l_margin - pdf.r_margin

    def h1(text: str) -> None:
        pdf.ln(2)
        pdf.set_font("Ru", "", 10)
        pdf.set_text_color(20, 55, 100)
        pdf.cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Ru", "", 8.5)

    def p(text: str) -> None:
        pdf.multi_cell(w, 4.0, text)
        pdf.ln(0.5)

    def bullet(text: str) -> None:
        pdf.multi_cell(w, 4.0, "  •  " + text)

    pdf.add_page()
    pdf.set_font("Ru", "", 13)
    pdf.cell(0, 7, "Отчёт о выполненной работе", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Ru", "", 8.5)
    pdf.cell(0, 4, "Проект PEM_07.2 — AI-генератор (CLI и веб-интерфейс)", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 4, "Дата отчёта: 26.06.2026", new_x="LMARGIN", new_y="NEXT")

    h1("1. Цель работы")
    p(
        "Разработать Python-приложение для взаимодействия с языковыми моделями и генерации "
        "изображений: консольный интерфейс, мультимодальный пайплайн (текст + изображение) "
        "и веб-интерфейс на Flask с формой ввода и отображением прогресса."
    )

    h1("2. Структура проекта (созданные файлы)")
    files = [
        "main.py — CLI (режимы chat и image)",
        "config.py — выбор провайдера, ключ ProxyAPI",
        "providers.py — OpenAI, GigaChat, ProxyAPI (gpt-image-1)",
        "pipeline.py — пайплайн GigaChat → ProxyAPI, сохранение в outputs/",
        "app.py — Flask-сервер, API /api/generate и /api/status",
        "templates/index.html, static/css/style.css, static/js/main.js — веб-форма и прогресс",
        "run_tests.py, run_multimodal_test.py, test_flask_api.py — тестовые скрипты",
        "requirements.txt, .env.example, README.md, .gitignore",
    ]
    for f in files:
        bullet(f)

    h1("3. Реализованный функционал")
    bullet("CLI: загрузка ключей из .env (python-dotenv), ввод запроса, вывод ответа.")
    bullet("Чат: OpenAI или GigaChat; при наличии обоих ключей выбирается GigaChat.")
    bullet("Мультимодальность: GigaChat улучшает промпт на английском, ProxyAPI генерирует PNG.")
    bullet("Каждый запуск сохраняет image.png, prompt_original.txt, prompt_refined.txt, metadata.json.")
    bullet("Flask: форма (режим + промпт), фоновая задача в потоке, опрос статуса раз в 1 с.")
    bullet("Прогресс-бар отображает этапы: улучшение промпта, генерация, сохранение.")

    h1("4. Зависимости (установленные версии)")
    bullet("python-dotenv 1.2.2, openai 2.44.0, gigachat 0.2.1, flask 3.1.3")

    h1("5. Промпты, использованные в Cursor")
    bullet("Создание CLI для OpenAI/GigaChat с ключами в .env и запуском python main.py.")
    bullet("Добавление мультимодальности: GigaChat + ProxyAPI, папка outputs, замер времени.")
    bullet("Преобразование в Flask с формой и прогрессом, тестирование на реальных API.")
    bullet("Формирование отчёта о проделанной работе.")

    h1("6. Проблемы при разработке и их решение")
    bullet("Отсутствие PROXY_API в .env — добавлена переменная, проверка в config.get_proxy_api_key().")
    bullet("ProxyAPI 402 (недостаточный баланс) — пополнение счёта на proxyapi.ru.")
    bullet("OpenAI 403 (регион не поддерживается) — при двух ключах приоритет перенесён на GigaChat.")
    bullet("Ключ OpenAI не подходит для ProxyAPI (401) — используется отдельный ключ PROXY_API.")
    bullet("Два процесса Flask на порту 5000 — завершение дубликатов, перезапуск одного экземпляра.")

    h1("7. Результаты тестирования")

    p("7.1. Автотест Flask (test_flask_api.py), 26.06.2026:")
    bullet("Главная страница — успешно.")
    bullet("Режим image: генерация PNG, проверка заголовка файла — успешно.")
    bullet("Режим chat через GigaChat — успешно.")
    bullet("Итог журнала: All tests passed.")

    p("7.2. Мультимодальные запуски (данные из outputs/*/metadata.json):")
    pdf.set_font("Ru", "", 7.5)
    col = [48, 22, 22, 22, 22]
    headers = ["Промпт", "GigaChat, с", "ProxyAPI, с", "Всего, с", "Сессия"]
    for i, h in enumerate(headers):
        pdf.cell(col[i], 4.5, h, border=1)
    pdf.ln()
    for r in runs:
        prompt = r["original_prompt"]
        if len(prompt) > 38:
            prompt = prompt[:35] + "..."
        t = r["timings_sec"]
        row = [
            prompt,
            str(t.get("gigachat_refine", "")),
            str(t.get("proxyapi_generate", "")),
            str(r.get("total_sec", "")),
            r.get("session_id", ""),
        ]
        for i, val in enumerate(row):
            pdf.cell(col[i], 4.5, val, border=1)
        pdf.ln()
    pdf.set_font("Ru", "", 8.5)
    p(f"Всего успешных генераций в outputs/: {len(runs)}.")

    p("7.3. CLI-тесты GigaChat (run_tests.py): три запроса («Привет!», «Что такое Python?», "
      "«Напиши функцию сортировки») — успешно в live-режиме.")

    h1("8. Вывод")
    p(
        "Поставленные задачи выполнены: создано консольное приложение, мультимодальный пайплайн "
        f"с {len(runs)} зафиксированными успешными генерациями изображений и веб-интерфейс Flask "
        "с формой и индикатором прогресса. Все автотесты API проходят. "
        "Запуск веб-версии: python app.py, адрес http://127.0.0.1:5000."
    )

    pdf.output(str(OUTPUT))
    print(f"Создан: {OUTPUT} ({len(runs)} записей в таблице)")


if __name__ == "__main__":
    build_report()
