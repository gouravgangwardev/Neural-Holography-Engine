"""
triposr_inference.py
=====================
Neural 3D Reconstruction Engine — TripoSR Backend
-------------------------------------------------

This module serves as the TripoSR-based reconstruction interface
for the Neural Holography Engine (NHE).

Function:
    Converts a single 2D image → 3D mesh (.glb) using TripoSR
    or compatible transformer-based reconstruction backends.

Integration:
    - Input from image_upload.py
    - Output consumed by mesh_optimizer.py and hologram_viewer.js
"""

import os
import torch
import numpy as np
from PIL import Image

# Optional imports for real TripoSR backend if installed
try:
    from triposr import TripoSRModel  # hypothetical import for real deployment
    TRIPOSR_AVAILABLE = True
except ImportError:
    TRIPOSR_AVAILABLE = False
    print("[WARN] TripoSR library not found. Running in mock mode.")

OUTPUT_DIR = "datasets/output_meshes/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_triposr_model(device="cuda" if torch.cuda.is_available() else "cpu"):
    """
    Load the TripoSR model (real or mock).
    Returns a model-like object with .infer(image) → mesh interface.
    """
    if TRIPOSR_AVAILABLE:
        model = TripoSRModel.from_pretrained("stabilityai/triposr")
        model.to(device)
        model.eval()
        print(f"[INFO] TripoSR model loaded on {device}")
        return model
    else:
        class MockTripoSR:
            def infer(self, image):
                # Simulate mesh generation
                print("[MOCK] Simulating 3D mesh generation from 2D input...")
                mesh_path = os.path.join(OUTPUT_DIR, "mock_output_mesh.glb")
                with open(mesh_path, "w") as f:
                    f.write("mock_3d_mesh_data")
                return mesh_path
        return MockTripoSR()


def preprocess_image(image_path, target_size=(512, 512)):
    """
    Load and prepare input image for TripoSR inference.
    Converts to tensor normalized in [0, 1].
    """
    img = Image.open(image_path).convert("RGB").resize(target_size)
    img_tensor = torch.tensor(np.array(img)).float() / 255.0
    img_tensor = img_tensor.permute(2, 0, 1).unsqueeze(0)  # BCHW format
    return img_tensor


def reconstruct_3d(image_path, model=None, device="cuda"):
    """
    Full reconstruction pipeline:
    1. Preprocess image
    2. Run TripoSR model inference
    3. Save output mesh (.glb)
    """
    print(f"[INFO] Starting reconstruction for {image_path}...")

    if model is None:
        model = load_triposr_model(device)

    # Preprocess
    image_tensor = preprocess_image(image_path)
    print("[INFO] Image preprocessed for model input.")

    # Inference
    mesh_path = model.infer(image_tensor)

    print(f"[SUCCESS] 3D mesh generated: {mesh_path}")
    return mesh_path


def batch_reconstruct(image_folder, limit=None):
    """
    Run 3D reconstruction for all images in a folder.
    Useful for dataset-wide hologram generation.
    """
    images = [
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.lower().endswith((".jpg", ".png", ".jpeg"))
    ]
    if limit:
        images = images[:limit]

    print(f"[INFO] Running batch reconstruction on {len(images)} images...")
    model = load_triposr_model()

    results = []
    for img_path in images:
        try:
            mesh = reconstruct_3d(img_path, model)
            results.append(mesh)
        except Exception as e:
            print(f"[ERROR] Failed on {img_path}: {e}")

    print(f"[INFO] Batch reconstruction complete: {len(results)} meshes saved.")
    return results


if __name__ == "__main__":
    # Command-line testing utility
    import argparse
    parser = argparse.ArgumentParser(description="Run TripoSR inference on a single image or folder.")
    parser.add_argument("input", type=str, help="Path to input image or folder")
    parser.add_argument("--batch", action="store_true", help="Enable batch mode")
    args = parser.parse_args()

    if args.batch and os.path.isdir(args.input):
        batch_reconstruct(args.input)
    else:
        reconstruct_3d(args.input)
