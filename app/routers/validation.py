from fastapi import APIRouter, File, UploadFile, Form

from app.services.face_validator import validate_uploaded_image
from app.services.facefusion_service import run_facefusion
from app.services.supabase_service import (
    download_video,
    get_lesson_by_id,
)
from app.services.file_service import save_uploaded_image

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "message": "Validation service is running."
    }

@router.post("/validate-face")
async def validate_face(file: UploadFile = File(...)):
    return await validate_uploaded_image(file)

@router.get("/download-test")
def download_test():

    local_file = download_video(
        bucket="lesson-videos",
        remote_path="history/mata_hari/video_base.mp4",
        local_path="storage/videos/video_base.mp4"
    )
    return {
        "status": "ok",
        "saved_to": local_file
    }

@router.get("/test-facefusion")
def test_facefusion():

    print("LOCAL IMAGE:", local_image)
    print("LOCAL VIDEO:", local_video)
    output = run_facefusion()

    return {
        "status": "ok",
        "video": output
    }

@router.post("/generate-video")
async def generate_video(
    lesson_id: str = Form(...),
    role: str = Form(...),
    language: str = Form(...),
    file: UploadFile = File(...)
):
        lesson = get_lesson_by_id(lesson_id)

        if role == "protagonist":
            if language == "es":
                video_path = lesson["protagonist_base_video_url_es"]
            else:
                video_path = lesson["protagonist_base_video_url_en"]
        else:
            if language == "es":
                video_path = lesson["witness_base_video_url_es"]
            else:
                video_path = lesson["witness_base_video_url_en"]

        local_video = download_video(
            bucket="lesson-videos",
            remote_path=video_path,
            local_path="storage/videos/base_video.mp4",
        )
        local_image = save_uploaded_image(file)
        output_video = run_facefusion(
        source_image=local_image,
        target_video=local_video,
        )

        return {
            "video_url": "http://192.168.100.13:8000/storage/outputs/result.mp4"
        }