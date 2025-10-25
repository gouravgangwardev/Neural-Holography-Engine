# Seed3D: Foundation Model for Universal 3D Assets

**Model Type:** Generative 3D Model  
**Institution:** ETH Zurich  
**Year:** 2025  
**Domain:** Cross-domain 3D asset generation  

---

## Overview

Seed3D is a foundation model capable of generating **universal 3D assets** from minimal inputs, suitable for holographic visualization, AR/VR, and digital twin applications.  
It supports diverse domains including objects, landscapes, and anatomical structures.

**Key Features:**
- Cross-domain 3D asset generation  
- Supports various input modalities (images, sketches, partial meshes)  
- Optimized for real-time inference with moderate GPU resources  
- Integrates seamlessly into Python and web-based 3D pipelines  

---

## Folder Contents

- `model_weights.pt` → Placeholder for the pretrained model  
- `config.json` → Default configuration parameters (input size, device, batch size, inference mode)  
- `README.md` → Model description and usage instructions  

---

## Installation / Usage

1. Install required Python packages (see main repo `requirements.txt`).  
2. Load the model in Python:

python
from seed3d import Seed3DModel

# Load pretrained model
model = Seed3DModel.from_pretrained("ethz/seed3d")
model.to("cuda")
model.eval()

# Example inference
mesh = model.infer("path/to/input_image_or_sketch.jpg")
