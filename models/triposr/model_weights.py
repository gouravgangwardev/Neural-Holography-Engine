"""
models/triposr/model_weights.pt (Placeholder)

Purpose:
--------
This file simulates the presence of TripoSR pretrained weights for demonstration
and research purposes. It allows the Neural Holography Engine (NHE) repository
to appear complete without including multi-gigabyte model files.

Structure:
----------
- Minimal tensor to mimic model parameters.
- Compatible with torch.load() to integrate with stub inference scripts.
- Size: only a few kilobytes (mock).

Usage:
------
from torch import load
weights = load("models/triposr/model_weights.pt")
# weights can be passed to mock models for demo/testing
"""

import torch
import os

# Step 1: Ensure the folder exists
os.makedirs("models/triposr", exist_ok=True)

# Step 2: Create a minimal placeholder tensor
# Mimics a small part of model weights (1x1 tensor)
dummy_weights = torch.randn(1, 1)

# Step 3: Save tensor as model_weights.pt
torch.save(dummy_weights, "models/triposr/model_weights.pt")

# Step 4: Confirmation message
print("[INFO] Mock TripoSR model_weights.pt created successfully at 'models/triposr/'")
print("[INFO] File size: ~1-2 KB (placeholder only)")
print("[INFO] Can be loaded using torch.load() in inference scripts for demos")
