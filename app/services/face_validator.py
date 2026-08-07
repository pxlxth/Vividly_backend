import cv2
import numpy as np
from app.services.face_detection import detect_faces
from fastapi import UploadFile
from app.services.face_pose import check_face_pose
from app.services.blur_detection import check_blur
from app.services.lighting_detection import check_lighting
from app.services.face_position import check_face_position
from app.services.insightface_validation import check_insightface

async def validate_uploaded_image(file: UploadFile):

    image_bytes = await file.read()

    np_array = np.frombuffer(image_bytes, np.uint8)

    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    if image is None:
        return {
            "valid": False,
            "message": "Invalid image."
        }

    height, width = image.shape[:2]

    MIN_WIDTH = 512
    MIN_HEIGHT = 512

    if width < MIN_WIDTH or height < MIN_HEIGHT:
        return {
            "valid": False,
            "code": "LOW_RESOLUTION",
            "message": f"Minimum resolution is {MIN_WIDTH}x{MIN_HEIGHT}px."
        }
    face_result = detect_faces(image)

    if not face_result["valid"]:
        return face_result

    position_result = check_face_position(
        image,
        face_result["detection"]
    )

    if not position_result["valid"]:
        return position_result

    pose_result = check_face_pose(image)

    if not pose_result["valid"]:
        return pose_result

    blur_result = check_blur(image)

    if not blur_result["valid"]:
        return blur_result

    lighting_result = check_lighting(image)

    if not lighting_result["valid"]:
        return lighting_result

    insight_result = check_insightface(image)

    if not insight_result["valid"]:
        return insight_result

    position_result = check_face_position(
    image,
    face_result["detection"]
)

    if not position_result["valid"]:
        return position_result
    
    insight_result = check_insightface(image)
    if not insight_result["valid"]:
        return insight_result

    return {
        "valid": True,
        "width": width,
        "height": height,
        "message": "Image loaded successfully."
    }
    