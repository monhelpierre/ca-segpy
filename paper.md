---
title: "CA-SegPy: An Open-Source Python Implementation of Cellular Automata-Based Image Segmentation"
tags:
  - Python
  - image segmentation
  - cellular automata
  - reproducibility
  - computer vision
authors:
  - name: Monhel Maudoony Pierre
    orcid: 0009-0004-2637-7997
    affiliation: 1
affiliations:
  - name: Universidade Federal de Uberlândia
    index: 1
date: 2025-10-23
bibliography: paper.bib
---

# Summary

Cellular Automata (CA) provide a flexible framework for modeling complex spatial dynamics and have recently been applied to image segmentation tasks. However, reproducibility of CA-based segmentation research has been limited due to the lack of publicly available implementations.

**CA-SegPy** offers a complete, open-source Python implementation of the CA-based image segmentation algorithm described by Ascencio-Piña et al. (2024) in *Heliyon*. The algorithm operates in three phases: two iterative neighborhood-based updates (with 3×3 and 5×5 neighborhoods) followed by a quantization-based segmentation stage. The implementation also includes built-in evaluation metrics (PSNR, SSIM), dataset integration (BSDS300 via KaggleHub), and visualization utilities.

CA-SegPy improves reproducibility by providing a transparent and modular codebase that researchers can extend, evaluate, and compare with other methods. The project emphasizes accessibility, clarity, and open scientific practices.

# Statement of Need

Despite promising qualitative results of the original CA segmentation method, the absence of an official implementation limits adoption and verification. **CA-SegPy** addresses this gap by providing a robust Python package that:

1. Reproduces the method described by Ascencio-Piña et al. (2024).
2. Integrates reproducibility tools (evaluation metrics, dataset loading).
3. Enables parameter tuning and experimentation.
4. Supports easy comparison with modern segmentation techniques.

By making the implementation publicly available, CA-SegPy contributes to the broader open-science movement in computer vision and image analysis.

# Features

- Reproduction of the CA-based segmentation algorithm.
- Modular design (core processing, evaluation, and utility modules).
- Quantitative evaluation using PSNR and SSIM metrics.
- Dataset loader for BSDS300 benchmark.
- Example notebooks and visual outputs for reproducibility.

# Acknowledgements

This implementation is inspired by *Image Segmentation with Cellular Automata* by Ascencio-Piña et al. (2024), published in *Heliyon* ([DOI: 10.1016/j.heliyon.2024.e31152](https://doi.org/10.1016/j.heliyon.2024.e31152)).

# References

```bibtex
@article{ascencio2024image,
  title={Image Segmentation with Cellular Automata},
  author={Ascencio-Pi{\~n}a, et al.},
  journal={Heliyon},
  year={2024},
  volume={10},
  pages={e31152},
  doi={10.1016/j.heliyon.2024.e31152}
}
