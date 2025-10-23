import os
import cv2


def load_grayscale_image(path):
    """Load an image in grayscale mode."""
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def list_images_in_folder(folder):
    """Return list of image paths from a directory."""
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
