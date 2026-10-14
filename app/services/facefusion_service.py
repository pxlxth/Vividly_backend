import subprocess
import uuid

from pathlib import Path

FACEFUSION_PATH = Path("/home/doriamedinarojascarla/facefusion")
PYTHON_EXECUTABLE = "python3"

BASE_DIR = Path(__file__).resolve().parents[2]

unique_id = str(uuid.uuid4())
OUTPUT_VIDEO = BASE_DIR / "storage" / "outputs" / f"result_{unique_id}.mp4"


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

    import os

    final_output = str(OUTPUT_VIDEO).replace(".mp4", "_final.mp4")

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", str(OUTPUT_VIDEO),
        "-i", target_video,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        final_output
    ])

    import os
    print("FINAL:", final_output)
    print("EXISTE FINAL?:", os.path.exists(final_output))

    return final_output
