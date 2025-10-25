# CRM: Dual-View CNN for 3D Reconstruction

**Model Type:** Neural 3D Reconstruction  
**Institution:** Tsinghua University  
**Year:** 2024  
**Domain:** Dual-view cardiac / anatomical 3D reconstruction  

---

## Overview

CRM is a convolutional neural network designed for **dual-view 3D reconstruction** of anatomical structures, especially the heart and other medical organs.  
It generates high-precision 3D meshes suitable for **medical simulation, holographic visualization, and research applications**.

**Key Features:**
- High anatomical accuracy (up to 97%)  
- Dual-view input for improved depth estimation  
- Optimized for moderate GPU inference speed  
- Integrates into Python and web-based 3D pipelines  

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
from crm import CRMModel

# Load pretrained model
model = CRMModel.from_pretrained("tsinghua/crm")
model.to("cuda")
model.eval() 

# Example inference on dual-view images
mesh = model.infer(["path/to/view1.jpg", "path/to/view2.jpg"])

## Configuration (`config.json`)

json
{
  "model_name": "CRM",
  "description": "Dual-view CNN for 3D anatomical reconstruction",
  "input_size": 512,
  "voxel_resolution": 128,
  "device": "cuda",
  "batch_size": 1,
  "precision": "float32",
  "normalization": "0-1",
  "inference_mode": "mock",
  "output_format": "glb",
  "notes": "Placeholder configuration for research/demo. Replace 'inference_mode' with 'real' for actual pretrained weights."
}

@article{crm2024,
  title={CRM: Dual-View Convolutional Neural Network for 3D Reconstruction},
  author={Tsinghua University},
  year={2024},
  url={https://example.com/crm-paper}
}
