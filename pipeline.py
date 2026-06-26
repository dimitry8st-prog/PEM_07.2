"""Мультимодальный пайплайн: текст (GigaChat) → изображение (ProxyAPI)."""

import json
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

from providers import GigaChatProvider, ProxyAPIImageProvider

OUTPUTS_DIR = Path("outputs")

REFINE_SYSTEM_PROMPT = (
    "Ты — эксперт по созданию детальных промптов для генерации изображений. "
    "Улучши пользовательский промпт: добавь стиль, композицию, освещение и палитру. "
    "Ответь ТОЛЬКО улучшенным промптом на английском языке, без пояснений."
)


@dataclass
class PipelineResult:
    session_id: str
    original_prompt: str
    refined_prompt: str
    image_path: str
    output_dir: str
    timings_sec: dict[str, float]
    total_sec: float

    def to_dict(self) -> dict:
        return asdict(self)


def _create_session_dir(base_dir: Path = OUTPUTS_DIR) -> tuple[str, Path]:
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = base_dir / session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    return session_id, session_dir


def run_multimodal_pipeline(prompt: str, output_dir: Path | None = None) -> PipelineResult:
    """Улучшает промпт через GigaChat и генерирует изображение через ProxyAPI."""
    total_start = time.perf_counter()
    timings: dict[str, float] = {}

    session_id, session_dir = _create_session_dir() if output_dir is None else (
        output_dir.name,
        output_dir,
    )
    session_dir.mkdir(parents=True, exist_ok=True)

    gigachat = GigaChatProvider()

    refine_start = time.perf_counter()
    print("  → GigaChat: улучшение промпта...")
    refined_prompt = gigachat.refine_image_prompt(prompt, REFINE_SYSTEM_PROMPT)
    timings["gigachat_refine"] = round(time.perf_counter() - refine_start, 3)
    print(f"  ✓ GigaChat: {timings['gigachat_refine']} сек")

    proxyapi = ProxyAPIImageProvider()
    image_start = time.perf_counter()
    print("  → ProxyAPI: генерация изображения...")
    image_bytes = proxyapi.generate_image(refined_prompt)
    timings["proxyapi_generate"] = round(time.perf_counter() - image_start, 3)
    print(f"  ✓ ProxyAPI: {timings['proxyapi_generate']} сек")

    save_start = time.perf_counter()
    image_path = session_dir / "image.png"
    image_path.write_bytes(image_bytes)

    (session_dir / "prompt_original.txt").write_text(prompt, encoding="utf-8")
    (session_dir / "prompt_refined.txt").write_text(refined_prompt, encoding="utf-8")
    timings["save_files"] = round(time.perf_counter() - save_start, 3)

    total_sec = round(time.perf_counter() - total_start, 3)
    timings["total"] = total_sec

    result = PipelineResult(
        session_id=session_id,
        original_prompt=prompt,
        refined_prompt=refined_prompt,
        image_path=str(image_path),
        output_dir=str(session_dir),
        timings_sec=timings,
        total_sec=total_sec,
    )

    (session_dir / "metadata.json").write_text(
        json.dumps(result.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return result
