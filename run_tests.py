#!/usr/bin/env python3
"""Скрипт для проверки CLI с тремя тестовыми запросами."""

import os
import sys
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

QUERIES = [
    "Привет!",
    "Что такое Python?",
    "Напиши функцию сортировки.",
]

MOCK_RESPONSES = {
    "Привет!": "Привет! Чем могу помочь?",
    "Что такое Python?": (
        "Python — высокоуровневый язык программирования общего назначения "
        "с простым синтаксисом и богатой экосистемой библиотек."
    ),
    "Напиши функцию сортировки.": (
        "def bubble_sort(arr):\n"
        "    n = len(arr)\n"
        "    for i in range(n):\n"
        "        for j in range(0, n - i - 1):\n"
        "            if arr[j] > arr[j + 1]:\n"
        "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n"
        "    return arr"
    ),
}


def _has_api_key() -> bool:
    load_dotenv()
    return bool(os.getenv("OPENAI_API_KEY", "").strip()) or bool(
        os.getenv("GIGACHAT_API_KEY", "").strip()
    )


def run_live_tests() -> list[dict]:
    from config import detect_provider
    from providers import get_provider

    provider_name = detect_provider()
    provider = get_provider(provider_name)
    results = []

    print(f"Режим: LIVE API ({provider_name})\n")

    for query in QUERIES:
        print(f"Запрос: {query}")
        try:
            response = provider.send_message(query)
            print(f"Ответ: {response}\n")
            results.append({"query": query, "response": response, "error": None})
        except Exception as exc:
            print(f"Ошибка: {exc}\n")
            results.append({"query": query, "response": None, "error": str(exc)})

    return results


def run_mock_tests() -> list[dict]:
    from providers import OpenAIProvider

    results = []
    print("Режим: MOCK (API-ключ не найден в .env)\n")

    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = lambda **kwargs: MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content=MOCK_RESPONSES[kwargs["messages"][0]["content"]]
                )
            )
        ]
    )

    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}, clear=False):
        with patch("openai.OpenAI", return_value=mock_client):
            provider = OpenAIProvider()
            for query in QUERIES:
                print(f"Запрос: {query}")
                response = provider.send_message(query)
                print(f"Ответ: {response}\n")
                results.append({"query": query, "response": response, "error": None})

    return results


def main() -> None:
    results = run_live_tests() if _has_api_key() else run_mock_tests()
    failed = [r for r in results if r["error"]]
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
