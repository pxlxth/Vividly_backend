from insightface.app import FaceAnalysis

face_app = FaceAnalysis()

face_app.prepare(
    ctx_id=0,
    det_size=(640, 640)
)

def check_insightface(image):

    faces = face_app.get(image)

    if len(faces) == 0:
        return {
            "valid": False,
            "code": "INSIGHTFACE_FAILED",
            "message": "The face could not be processed."
        }

    if len(faces) > 1:
        return {
            "valid": False,
            "code": "MULTIPLE_FACES",
            "message": "More than one face detected."
        }

    return {
        "valid": True
    }