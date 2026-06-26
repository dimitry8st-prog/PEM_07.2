#!/usr/bin/env python3
"""Тест полного мультимодального цикла с замером времени."""

import sys

from dotenv import load_dotenv

from pipeline import run_multimodal_pipeline

TEST_PROMPT = "Кот-астронавт на фоне звёздного неба"


def main() -> None:
    load_dotenv()

    print("=== Мультимодальный тест ===")
    print(f"Промпт: {TEST_PROMPT}\n")

    try:
        result = run_multimodal_pipeline(TEST_PROMPT)
    except Exception as exc:
        print(f"ОШИБКА: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Исходный промпт:")
    print(f"  {result.original_prompt}\n")
    print("Улучшенный промпт:")
    print(f"  {result.refined_prompt}\n")
    print(f"Изображение: {result.image_path}")
    print(f"Папка результатов: {result.output_dir}\n")
    print("Время выполнения (сек):")
    for step, seconds in result.timings_sec.items():
        print(f"  {step}: {seconds}")
    print(f"\nИтого: {result.total_sec} сек")
    sys.exit(0)


if __name__ == "__main__":
    main()
