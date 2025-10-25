# TripoSR: Transformer-based Single-Image 3D Reconstruction

**Model Type:** Neural 3D Reconstruction  
**Institution:** Stability AI  
**Year:** 2024  
**Domain:** Single-image → 3D mesh  

---

## Overview

TripoSR is a transformer-based model designed to reconstruct a full 3D mesh from a single 2D image.  
It is optimized for **real-time inference**, making it suitable for holographic applications like the Neural Holography Engine (NHE).

**Key Features:**
- Sub-second reconstruction speed
- High-quality mesh generation
- Compatible with various domains: faces, objects, and small-scale environments
- Integrates easily into Python pipelines or web-based 3D viewers

---

## Folder Contents

- `model_weights.pt` → Placeholder for the pretrained model  
- `config.json` → Default configuration parameters (input size, device, batch size)  
- `README.md` → Model description and usage instructions

---

## Installation / Usage

1. Install required Python packages (see main repo `requirements.txt`).  
2. Load the model in Python:

```python
from triposr import TripoSRModel

# Load pretrained model
model = TripoSRModel.from_pretrained("stabilityai/triposr")
model.to("cuda")
model.eval()

# Example inference
mesh = model.infer("path/to/input_image.jpg")
Mesh output is typically `.glb` or `.obj`, ready for Three.js visualization or holographic projection.

---

## Configuration (`config.json`)

```json
{
  "input_size": 512,
  "voxel_resolution": 128,
  "device": "cuda",
  "batch_size": 1
}

@article{triposr2024,
  title={TripoSR: Transformer-based Single-Image 3D Reconstruction},
  author={Stability AI},
  year={2024},
  url={https://huggingface.co/stabilityai/triposr}
}
