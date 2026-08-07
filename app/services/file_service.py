from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

def save_uploaded_image(file):
    output_path = BASE_DIR / "storage" / "uploads" / "source.jpg"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as buffer:
        buffer.write(file.file.read())

    return str(output_path)