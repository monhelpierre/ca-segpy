"""
ca_segpy: Cellular Automata-based Image Segmentation Toolkit
"""

from .utils import list_images_in_folder, load_grayscale_image
from .runner import run_ca, ca_image_segmentation
from .evaluation import evaluate_segmentation

# Assign top-level names
list_images_in_folder = list_images_in_folder
load_grayscale_image = load_grayscale_image
run_ca = run_ca
ca_image_segmentation = ca_image_segmentation
evaluate_segmentation = evaluate_segmentation

__all__ = [
    "list_images_in_folder",
    "load_grayscale_image",
    "run_ca",
    "ca_image_segmentation",
    "evaluate_segmentation",
]


__version__ = "0.1.0"
