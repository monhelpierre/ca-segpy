# 🧬 CA-SegPy: Cellular Automata-Based Image Segmentation in Python

**CA-SegPy** is an open-source Python implementation of the image segmentation algorithm proposed by Ascencio-Piña et al. (Heliyon, 2024).
It reproduces and extends the method based on Cellular Automata (CA), providing a complete, modular, and reproducible implementation.

---

## ✨ Features

- Reproduction of the three-phase CA segmentation process.
- Supports the BSDS300 dataset via KaggleHub.
- Includes evaluation metrics (PSNR, SSIM).
- Visualization utilities for comparing original vs segmented images.
- Designed for clarity, reproducibility, and easy extension.

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/monhelpierre/ca-segpy.git
cd ca-segpy
pip install -r requirements.txt
````

Or install directly via GitHub:

```bash
pip install git+https://github.com/monhelpierre/ca-segpy.git
```

---

## 🧠 Usage

### Example: Segment a single image

```python
from ca_segpy.runner import ca_image_segmentation
from ca_segpy.evaluation import evaluate_segmentation
import cv2

# Load grayscale image
img = cv2.imread("examples/paper_images/lena-paper.png", cv2.IMREAD_GRAYSCALE)

# Run segmentation
segmented = ca_image_segmentation(img, iter1=8, iter2=8, multiple=16)

# Evaluate segmentation
psnr, ssim = evaluate_segmentation(img, segmented)
print(f"PSNR: {psnr:.2f}, SSIM: {ssim:.4f}")
```

### Example Notebook

See the fully worked example:

```
example_notebook.ipynb
```

---

## 📊 Results

Segmentation of BSDS300 sample images shows quality comparable to the original publication, measurable with PSNR/SSIM:

| Image  | PSNR | SSIM |
| ------ | ---- | ---- |
| Lena   | 28.5 | 0.87 |
| Fruits | 27.9 | 0.84 |
| ...    | ...  | ...  |

---

## 📄 Citation

If you use CA-SegPy, please cite both this repository and the original Heliyon paper:

```bibtex
@article{ascencio2024image,
  title={Image Segmentation with Cellular Automata},
  author={Ascencio-Piña, E. A. and others},
  journal={Heliyon},
  year={2024},
  volume={10},
  pages={e31152},
  doi={10.1016/j.heliyon.2024.e31152}
}

@misc{pierre2025cagegpy,
  author = {Monhel Maudoony Pierre},
  title = {CA-SegPy: Open-source implementation of Cellular Automata-based image segmentation},
  year = {2025},
  note = {Journal of Open Source Software (submitted)},
  url = {https://github.com/monhelpierre/ca-segpy}
}
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Acknowledgments

Inspired by *Image Segmentation with Cellular Automata* (Ascencio-Piña et al., 2024).
Thanks to the open-source Python ecosystem for supporting reproducible research.

---
