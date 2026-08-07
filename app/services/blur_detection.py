import cv2


def check_blur(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    print(f"Blur score: {variance}")

    MIN_VARIANCE = 50

    if variance < MIN_VARIANCE:
        return {
            "valid": False,
            "code": "BLURRY_IMAGE",
            "message": "The image is blurry. Please upload a sharper photo.",
            "blur_score": round(variance, 2),
        }

    return {
        "valid": True,
        "blur_score": round(variance, 2),
    }