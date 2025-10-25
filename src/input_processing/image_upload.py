"""
================
Module for handling image uploads and preprocessing for the Neural Holography Engine (NHE).

Features:
- Upload images from local filesystem or web input
- Validate formats (PNG, JPG, JPEG)
- Optional resizing and normalization for model readiness
- Stores images in structured dataset folders
"""

import os
from PIL import Image
import numpy as np

# Supported image formats
SUPPORTED_FORMATS = ("png", "jpg", "jpeg")
UPLOAD_DIR = "datasets/input_images/"

def ensure_upload_dir():
    """Ensure the upload directory exists."""
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
        print(f"[INFO] Created upload directory: {UPLOAD_DIR}")

def validate_image(file_path):
    """Check if the uploaded file is a supported image."""
    ext = file_path.lower().split(".")[-1]
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported file type: {ext}. Supported formats: {SUPPORTED_FORMATS}")
    return True

def preprocess_image(file_path, target_size=(512, 512), normalize=True):
    """
    Preprocess image for neural 3D reconstruction.
    - Resize to target_size
    - Convert to RGB
    - Optionally normalize pixel values to [0,1]
    """
    with Image.open(file_path) as img:
        img = img.convert("RGB")
        img = img.resize(target_size)
        img_array = np.array(img, dtype=np.float32)
        if normalize:
            img_array /= 255.0
        return img_array

def save_image(file_path, new_name=None):
    """Save image to upload directory with optional new name."""
    ensure_upload_dir()
    validate_image(file_path)
    
    # Determine save path
    base_name = new_name if new_name else os.path.basename(file_path)
    save_path = os.path.join(UPLOAD_DIR, base_name)
    
    # Open and save using PIL
    try:
        with Image.open(file_path) as img:
            img.save(save_path)
            print(f"[INFO] Image saved to: {save_path}")
            return save_path
    except Exception as e:
        raise IOError(f"Failed to process image: {e}")

def list_uploaded_images():
    """Return a list of all uploaded images."""
    ensure_upload_dir()
    return [f for f in os.listdir(UPLOAD_DIR) if f.lower().endswith(SUPPORTED_FORMATS)]

if __name__ == "__main__":
    # Simple CLI for testing
    import argparse
    parser = argparse.ArgumentParser(description="Upload and preprocess images for NHE processing.")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("--rename", type=str, help="Optional new name for the uploaded file")
    parser.add_argument("--preview", action="store_true", help="Preview preprocessed image")
    args = parser.parse_args()

    try:
        saved_path = save_image(args.image_path, args.rename)
        preprocessed = preprocess_image(saved_path)
        print(f"[SUCCESS] Image uploaded and preprocessed: {saved_path}")
        if args.preview:
            import matplotlib.pyplot as plt
            plt.imshow(preprocessed)
            plt.title("Preprocessed Image Preview")
            plt.axis("off")
            plt.show()
    except Exception as ex:
        print(f"[ERROR] {ex}")
