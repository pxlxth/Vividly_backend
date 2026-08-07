import subprocess
from pathlib import Path

FACEFUSION_PATH = Path(
    r"C:\Users\CSAENCUser\Desktop\Facefusion app\facefusion"
)
PYTHON_EXECUTABLE = r"C:\Users\CSAENCUser\miniconda3\python.exe"

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_VIDEO = BASE_DIR / "storage" / "outputs" / "result.mp4"


def run_facefusion(
    source_image: str,
    target_video: str,
):  
    OUTPUT_VIDEO.parent.mkdir(parents=True, exist_ok=True)

    command = [
        PYTHON_EXECUTABLE,
        str(FACEFUSION_PATH / "facefusion.py"),
        "headless-run",
        "-s",
        source_image,
        "-t",
        target_video,
        "-o",
        str(OUTPUT_VIDEO),
         "--processors", "face_swapper",
        "--face-swapper-model", "ghost_1_256",
        "--face-enhancer-model", "gfpgan_1.4",
        "--face-enhancer-blend", "80",
    ]
    print("Comando:")
    print(command)
    result = subprocess.run(
        command,
        cwd=FACEFUSION_PATH,
        capture_output=True,
        text=True
    )
    print("RETURN CODE:", result.returncode)
    print("STDOUT:")
    print(result.stdout)
    print("STDERR:")
    print(result.stderr)

    if result.returncode != 0:
        raise Exception(result.stderr)

    return str(OUTPUT_VIDEO)