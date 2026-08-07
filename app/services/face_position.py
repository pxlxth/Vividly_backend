def check_face_position(image, detection):

    bbox = detection.location_data.relative_bounding_box

    center_x = bbox.xmin + (bbox.width / 2)
    center_y = bbox.ymin + (bbox.height / 2)

    MIN_X = 0.30
    MAX_X = 0.70

    MIN_Y = 0.30
    MAX_Y = 0.70

    if not (MIN_X <= center_x <= MAX_X):
        return {
            "valid": False,
            "code": "FACE_NOT_CENTERED",
            "message": "Center your face in the frame."
        }

    if not (MIN_Y <= center_y <= MAX_Y):
        return {
            "valid": False,
            "code": "FACE_NOT_CENTERED",
            "message": "Center your face in the frame."
        }

    return {
        "valid": True
    }