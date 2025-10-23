from skimage.metrics import (
    structural_similarity as ssim,
    peak_signal_noise_ratio as psnr,
)


def evaluate_segmentation(original, segmented):
    """
    Compute PSNR and SSIM between original and segmented images.
    """
    if original.shape != segmented.shape:
        raise ValueError("Original and segmented images must have the same dimensions.")
    psnr_value = psnr(original, segmented, data_range=255)
    ssim_value = ssim(original, segmented, data_range=255)
    return psnr_value, ssim_value
