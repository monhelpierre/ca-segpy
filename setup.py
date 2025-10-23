from setuptools import setup, find_packages

setup(
    name="ca_segpy",
    version="0.1.0",
    author="Monhel Maudoony Pierre",
    author_email="monhelmaudoopierre@gmail.com",
    description="Python implementation of Cellular Automata-based Image Segmentation (Heliyon 2024)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.8",
)
