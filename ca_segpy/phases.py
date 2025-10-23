import numpy as np
from .core import majority_function


def phases_process(image, radius, iterations):
    """
    Applies Cellular Automata updates using a neighborhood of size (2r+1)x(2r+1).
    """
    updated_image = np.pad(image, pad_width=radius, mode="edge")
    for _ in range(iterations):
        for i in range(radius, updated_image.shape[0] - radius):
            for j in range(radius, updated_image.shape[1] - radius):
                neighborhood = [
                    updated_image[x, y]
                    for x in range(i - radius, i + radius + 1)
                    for y in range(j - radius, j + radius + 1)
                ]
                updated_image[i, j] = majority_function(
                    updated_image[i, j], neighborhood
                )
    return updated_image[radius:-radius, radius:-radius]


def phase1(image, iterations=8):
    """Phase 1: 3x3 neighborhood."""
    return phases_process(image, radius=1, iterations=iterations)


def phase2(image, iterations=8):
    """Phase 2: 5x5 neighborhood."""
    return phases_process(image, radius=2, iterations=iterations)


def phase3(image, multiple=16):
    """Phase 3: Quantization of pixel values."""
    image = np.round(image / multiple) * multiple
    return image.astype(np.uint8)
