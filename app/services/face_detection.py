import cv2
import mediapipe as mp


mp_face_detection = mp.solutions.face_detection
face_detector = mp_face_detection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.6,
)

def detect_faces(image):

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detector.process(rgb_image)

    print("========== FACE DETECTION ==========")
    print(results)
    print(results.detections)
    print("====================================")

    if results.detections is None:
        return {
            "valid": False,
            "code": "NO_FACE",
            "message": "No face detected.",
            "face_count": 0,
        }

    face_count = len(results.detections)
    detection = results.detections[0]
    bbox = detection.location_data.relative_bounding_box
    image_height, image_width = image.shape[:2]
    face_width = bbox.width * image_width
    face_height = bbox.height * image_height

    face_area = face_width * face_height
    image_area = image_width * image_height

    face_percentage = (face_area / image_area) * 100

    print(f"Faces detected: {face_count}")

    if face_count > 1:
        return {
            "valid": False,
            "code": "MULTIPLE_FACES",
            "message": "More than one face detected.",
            "face_count": face_count,
        }
    MIN_FACE_PERCENTAGE = 8

    if face_percentage < MIN_FACE_PERCENTAGE:
        return {
            "valid": False,
            "code": "FACE_TOO_SMALL",
            "message": "Move closer to the camera.",
            "face_percentage": round(face_percentage, 2),
        }   

    return {
        "valid": True,
        "face_count": 1,
        "face_percentage": round(face_percentage, 2),
        "detection": detection,
    }
