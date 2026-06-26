#!/usr/bin/env python3
"""CLI-приложение: чат (OpenAI/GigaChat) и мультимодальная генерация изображений."""

import argparse
import sys

from dotenv import load_dotenv

from config import detect_provider
from pipeline import run_multimodal_pipeline
from providers import GigaChatProvider, ProxyAPIImageProvider, get_provider


def run_chat_mode() -> None:
    try:
        provider_name = detect_provider()
        provider = get_provider(provider_name)
    except ValueError as exc:
        print(f"Ошибка конфигурации: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Используется провайдер: {provider_name}")
    print("Введите запрос (Ctrl+C или пустая строка для выхода):\n")

    try:
        user_input = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nВыход.")
        sys.exit(0)

    if not user_input:
        print("Запрос не введён. Выход.")
        sys.exit(0)

    try:
        response = provider.send_message(user_input)
    except Exception as exc:
        print(f"\nОшибка при обращении к API: {exc}", file=sys.stderr)
        sys.exit(1)

    print("\n--- Ответ ---\n")
    print(response)


def run_image_mode() -> None:
    try:
        GigaChatProvider()
        ProxyAPIImageProvider()
    except ValueError as exc:
        print(f"Ошибка конфигурации: {exc}", file=sys.stderr)
        print(
            "Для мультимодального режима нужны GIGACHAT_API_KEY и PROXY_API в .env",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Мультимодальный режим: GigaChat (текст) → ProxyAPI (изображение)")
    print("Введите описание изображения:\n")

    try:
        user_input = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nВыход.")
        sys.exit(0)

    if not user_input:
        print("Промпт не введён. Выход.")
        sys.exit(0)

    print("\n[1/2] Улучшение промпта через GigaChat...")
    try:
        result = run_multimodal_pipeline(user_input)
    except Exception as exc:
        print(f"\nОшибка пайплайна: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"[2/2] Изображение сохранено: {result.image_path}")
    print("\n--- Улучшенный промпт ---\n")
    print(result.refined_prompt)
    print("\n--- Время выполнения (сек) ---")
    for step, seconds in result.timings_sec.items():
        print(f"  {step}: {seconds}")
    print(f"\nРезультаты сохранены в: {result.output_dir}")


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="CLI для OpenAI/GigaChat и мультимодальной генерации изображений"
    )
    parser.add_argument(
        "--mode",
        choices=["chat", "image"],
        default="chat",
        help="chat — текстовый чат; image — GigaChat + ProxyAPI",
    )
    args = parser.parse_args()

    if args.mode == "image":
        run_image_mode()
    else:
        run_chat_mode()


if __name__ == "__main__":
    main()
