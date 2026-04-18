from __future__ import annotations

import json
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "Mind" / "Fonte temp"
OUTPUT_DIR = SOURCE_DIR / "ingestao"

PDFS = {
    "cfg": SOURCE_DIR / "Apostila CFG 2025.pdf",
    "cga": SOURCE_DIR / "Apostila CGA 2025.pdf",
    "cge": SOURCE_DIR / "Apostila CGE 2025.pdf",
}

TOC_PATTERN = re.compile(r"(sum[aá]rio|[ií]ndice)", re.IGNORECASE)


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_toc_excerpt(reader: PdfReader, max_pages: int = 12) -> str:
    excerpts: list[str] = []
    for index, page in enumerate(reader.pages[:max_pages]):
        text = clean_text(page.extract_text() or "")
        if not text:
            continue
        if index <= 3 or TOC_PATTERN.search(text):
            excerpts.append(f"=== PAGE {index + 1} ===\n{text[:5000]}")
    return "\n\n".join(excerpts).strip()


def write_pdf_outputs(name: str, pdf_path: Path) -> None:
    reader = PdfReader(str(pdf_path))
    target_dir = OUTPUT_DIR / name
    pages_dir = target_dir / "pages"
    target_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)

    full_text_parts: list[str] = []

    for index, page in enumerate(reader.pages, start=1):
        text = clean_text(page.extract_text() or "")
        page_header = f"=== PAGE {index} ==="
        page_payload = f"{page_header}\n{text}\n"
        full_text_parts.append(page_payload)
        (pages_dir / f"page-{index:04d}.txt").write_text(page_payload, encoding="utf-8")

    metadata = {
        "source_pdf": str(pdf_path.relative_to(ROOT)),
        "page_count": len(reader.pages),
        "output_dir": str(target_dir.relative_to(ROOT)),
    }

    (target_dir / "full_text.txt").write_text("\n".join(full_text_parts), encoding="utf-8")
    (target_dir / "toc_excerpt.txt").write_text(extract_toc_excerpt(reader), encoding="utf-8")
    (target_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, pdf_path in PDFS.items():
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF não encontrado: {pdf_path}")
        write_pdf_outputs(name, pdf_path)


if __name__ == "__main__":
    main()
