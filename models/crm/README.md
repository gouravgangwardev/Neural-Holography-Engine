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
