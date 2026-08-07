import cv2
import numpy as np


def check_lighting(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    MIN_BRIGHTNESS = 60
    MAX_BRIGHTNESS = 190

    if brightness < MIN_BRIGHTNESS:
        return {
            "valid": False,
            "code": "LOW_LIGHT",
            "message": "The image is too dark. Please improve the lighting.",
            "brightness": round(float(brightness), 2),
        }

    if brightness > MAX_BRIGHTNESS:
        return {
            "valid": False,
            "code": "OVEREXPOSED",
            "message": "The image is too bright. Please avoid strong light.",
            "brightness": round(float(brightness), 2),
        }

    return {
        "valid": True,
        "brightness": round(float(brightness), 2),
    }