import os
import io
import base64
import argparse
import datetime as dt
from pathlib import Path

from loguru import logger
from dotenv import load_dotenv

from utils import (
    generate_with_references,
    generate_together,
)

# ======== additional ========

def b64_image(image_path: str) -> str | None:
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            buf = io.BytesIO()
            img.save(buf, format="JPEG")
            return base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception as e:
        logger.error(f"Failed to read image '{image_path}': {e}")
        return None

def as_int(val, default: int) -> int:
    try:
        return int(val)
    except Exception:
        return default

def as_float(val, default: float) -> float:
    try:
        return float(val)
    except Exception:
        return default

def as_bool(val, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    s = (val or "").strip().lower()
    if s in {"1","true","yes","y","on"}: return True
    if s in {"0","false","no","n","off"}: return False
    return default

def slugify(s: str, maxlen: int = 30) -> str:
    out = "".join(c if c.isalnum() or c in "-_." else "_" for c in s[:maxlen])
    return out or "query"

# ======== main ========

def run(
    text: str | None,
    image_path: str | None,
    image_prompt: str | None,
    rounds: int,
    multi_turn: bool,
    temperature: float,
    max_tokens: int,
    model_aggregate: str,
    reference_models: list[str],
    api1_base: str,
    api1_key: str,
    api2_base: str,
    api2_key: str,
    output_dir: Path,
):

    # Build user content
    if image_path:
        b64 = b64_image(image_path)
        if not b64:
            raise SystemExit("Image path invalid or unreadable.")
        content = [
            {"type": "text", "text": image_prompt or ""},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}" }},
        ]
        use_reference_models = False  # как в MoA.py для картинок
        logger.info("Run mode: IMAGE")
    else:
        if not text or not text.strip():
            raise SystemExit("No text to process.")
        content = text
        use_reference_models = True
        logger.info("Run mode: TEXT")

    # Prepare reference 
    references = []
    if use_reference_models and reference_models:
        references = [""] * len(reference_models)

        if multi_turn:
            histories = [[{"role": "user", "content": content}] for _ in reference_models]
        else:
            single_turn = [{"role": "user", "content": content}]

        for r in range(rounds):
            logger.info(f"Reference round {r+1}/{rounds}")
            for i, model in enumerate(reference_models):
                msgs = histories[i] if multi_turn else single_turn

                out = generate_with_references(
                    model=model,
                    messages=msgs,
                    references=references,
                    temperature=temperature,
                    max_tokens=max_tokens,

                ) or ""

                references[i] = out.strip()
                if multi_turn:
                    histories[i].append({"role": "assistant", "content": out})

    logger.info(f"Aggregating with model: {model_aggregate}")
    final = generate_with_references(
        model=model_aggregate,
        temperature=temperature,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": content}],
        references=references,
        generate_fn=generate_together,
        api_base=api2_base,
        api_key=api2_key,
    ) or ""

    # Save output
    output_dir.mkdir(parents=True, exist_ok=True)
    if isinstance(content, str):
        stem = slugify(content)
    else:
        # images
        stem = slugify(image_prompt or "image_query")

    name = output_dir.name
    out_path = output_dir / f"{name}.md"

    meta_lines = [
        f"# MoA run ({name})",
        "",
        "## Config",
        f"- Aggregate model: {model_aggregate}",
        f"- Reference models: {', '.join(reference_models) if reference_models else '(none)'}",
        f"- ROUNDS={rounds}, MULTITURN={multi_turn}",
        f"- TEMPERATURE={temperature}, MAX_TOKENS={max_tokens}",
        "",
    ]

    if use_reference_models and references:
        meta_lines.append("## Reference outputs")
        for i, (m, ref) in enumerate(zip(reference_models, references), start=1):
            meta_lines.append(f"### [{i}] {m}")
            meta_lines.append(ref if ref else "(empty)")
            meta_lines.append("")

    meta_lines.append("## Final answer (aggregate)")
    meta_lines.append(final.strip())

    out_path.write_text("\n".join(meta_lines), encoding="utf-8")
    print(f"\nSaved to: {out_path}")
    print("\n--- FINAL ANSWER ---\n")
    print(final.strip())
    print("\n--------------------\n")


def main():
    load_dotenv(override=True)

    API_BASE     = os.getenv("API_BASE", "")
    API_KEY      = os.getenv("API_KEY", "")
    API_BASE_2   = os.getenv("API_BASE_2", "")
    API_KEY_2    = os.getenv("API_KEY_2", "")

    MODEL_AGGREGATE = os.getenv("MODEL_AGGREGATE", "")
    MODEL_REFERENCE_1 = os.getenv("MODEL_REFERENCE_1", "")
    MODEL_REFERENCE_2 = os.getenv("MODEL_REFERENCE_2", "")
    MODEL_REFERENCE_3 = os.getenv("MODEL_REFERENCE_3", "")

    MAX_TOKENS  = as_int(os.getenv("MAX_TOKENS", 2048), 2048)
    TEMPERATURE = as_float(os.getenv("TEMPERATURE", 0.7), 0.7)
    ROUNDS      = as_int(os.getenv("ROUNDS", 1), 1)
    MULTITURN   = as_bool(os.getenv("MULTITURN", "False"), False)

    parser = argparse.ArgumentParser(description="Run MoA extraction without prompts.")
    g = parser.add_mutually_exclusive_group()
    g.add_argument("--text", type=str, help="Raw text to extract from.")
    g.add_argument("--text-file", type=str, help="Path to a UTF-8 text file.")
    g.add_argument("--image", type=str, help="Path to an image file.")
    parser.add_argument("--image-prompt", type=str, help="Optional instruction accompanying image.")
    parser.add_argument("--rounds", type=int, default=ROUNDS)
    parser.add_argument("--multi-turn", action="store_true" if MULTITURN else "store_false",
                        help=f"Enable multi-turn reference dialogue (default from .env MULTITURN={MULTITURN})")
    parser.add_argument("--temperature", type=float, default=TEMPERATURE)
    parser.add_argument("--max-tokens", type=int, default=MAX_TOKENS)
    parser.add_argument("--output-dir", type=str, default="moa_output")

    args = parser.parse_args()

    text = args.text
    if not text and args.text_file:
        text = Path(args.text_file).read_text(encoding="utf-8")
    if not text and INPUT_FILE:
        text = Path(INPUT_FILE).read_text(encoding="utf-8")
    if not text and INPUT_TEXT:
        text = INPUT_TEXT

    image_path = args.image or INPUT_IMAGE
    image_prompt = args.image_prompt if args.image_prompt is not None else IMAGE_PROMPT

    reference_models = [m for m in [MODEL_REFERENCE_1, MODEL_REFERENCE_2, MODEL_REFERENCE_3] if m]

    # Sanity
    if not MODEL_AGGREGATE:
        raise SystemExit("MODEL_AGGREGATE is not set in .env")
    if not image_path and not text:
        raise SystemExit("No input provided. Use --text/--text-file/--image or set INPUT_TEXT/INPUT_FILE/INPUT_IMAGE in .env")

    run(
        text=text,
        image_path=image_path,
        image_prompt=image_prompt,
        rounds=args.rounds,
        multi_turn=args.multi_turn,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        model_aggregate=MODEL_AGGREGATE,
        reference_models=reference_models,
        api1_base=API_BASE,
        api1_key=API_KEY,
        api2_base=API_BASE_2,
        api2_key=API_KEY_2,
        output_dir=Path(args.output_dir),
    )

if __name__ == "__main__":
    main()
