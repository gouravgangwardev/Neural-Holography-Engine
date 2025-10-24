"""
Neural Holography Engine - Setup Script
=======================================

Purpose:
- This setup.py makes the Neural Holography Engine (NHE) pip-installable.
- Designed as a **research-quality, theory-safe repository**.
- All dependencies are latest stable releases (unpinned) for credibility.
- Includes optional entry points, metadata, and package data.

Author: Vikrit
Version: 1.0.0
License: MIT
"""

from setuptools import setup, find_packages
import pathlib

# Get the directory containing this file
here = pathlib.Path(__file__).parent.resolve()

# Read long description from README.md
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    # Basic metadata
    name="SpectraCALL",
    version="1.0.0",
    author="Gourav Gangwar",
    description="A theoretical framework for neural 2D-to-3D holographic reconstruction and AI-driven spatial visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Package discovery
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,  # Include assets like diagrams and docs

    # Python version requirement
    python_requires=">=3.10",

    # Dependencies (latest versions)
    install_requires=[
        # Core AI & 3D
        "torch",
        "torchvision",
        "numpy",
        "scipy",

        # Image Processing
        "opencv-python",
        "mediapipe",
        "Pillow",

        # 3D Geometry & Rendering
        "trimesh",
        "open3d",
        "pythreejs",

        # Web & API
        "flask",
        "fastapi",
        "uvicorn",

        # Utilities
        "tqdm",
        "rich"
    ],

  
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            "black"
        ],
        "notebooks": [
            "jupyterlab",
            "plotly",
            "dash",
            "seaborn"
        ],
        "hardware": [
            "pyrealsense2",
            "leapmotion-sdk", 
            "azure-kinect"    
        ]
    },

)
    entry_points={
        "console_scripts": [
            "nhe-run=main:main",  # CLI command example; main:main should be a stub
        ],
    },


    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Operating System :: OS Independent"
    ],


    keywords="AI holography 2D-3D reconstruction neural rendering gesture control volumetric projection",
)
