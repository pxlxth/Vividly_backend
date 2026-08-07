import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.7,
)


def check_face_pose(image):

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return {
            "valid": False,
            "code": "NO_FACE",
            "message": "No face detected."
        }

    landmarks = results.multi_face_landmarks[0].landmark

    left_eye = landmarks[33]
    right_eye = landmarks[263]
    nose = landmarks[1]

    eye_center = (left_eye.x + right_eye.x) / 2

    difference = abs(nose.x - eye_center)

    MAX_DIFFERENCE = 0.05

    if difference > MAX_DIFFERENCE:
        return {
            "valid": False,
            "code": "FACE_NOT_FRONT",
            "message": "Please look directly at the camera."
        }

    return {
        "valid": True
    }