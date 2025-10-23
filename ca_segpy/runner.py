import matplotlib.pyplot as plt
from .phases import phase1, phase2, phase3
from .evaluation import evaluate_segmentation
from .utils import load_grayscale_image, list_images_in_folder


def ca_image_segmentation(image, iter1=8, iter2=8, multiple=16):
    """Complete 3-phase CA segmentation pipeline."""
    p1 = phase1(image, iter1)
    p2 = phase2(p1, iter2)
    return phase3(p2, multiple)


def run_ca(path, iter1=8, iter2=8, multiple=16, debug=False, limit=-1):
    """
    Run the CA segmentation and show visual + quantitative results.
    """

    result = []

    for path in list_images_in_folder(path)[:limit]:

        original = load_grayscale_image(path)
        segmented = ca_image_segmentation(original, iter1, iter2, multiple)
        psnr_val, ssim_val = evaluate_segmentation(original, segmented)

        if debug:
            print(f"PSNR: {psnr_val:.2f}, SSIM: {ssim_val:.4f}")

            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.imshow(original, cmap="gray")
            plt.title("Original")
            plt.axis("off")
            plt.subplot(1, 2, 2)
            plt.imshow(segmented, cmap="gray")
            plt.title("Segmented")
            plt.axis("off")
            plt.show()

        result.append(
            {
                "ssim": ssim_val,
                "psnr": psnr_val,
                "original": original,
                "segmented": segmented,
            }
        )

    return result
