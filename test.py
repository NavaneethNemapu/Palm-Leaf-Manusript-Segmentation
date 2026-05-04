import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Import your custom local U-Net architecture
from unet import UNet

# 1. Configuration
MODEL_WEIGHTS_PATH = r"C:\Users\navan\Desktop\palmleaf\best_model.pth"

# Ask for image path and clean it up
raw_path = input("\n👉 Enter the full path to your test image: ")
TEST_IMAGE_PATH = raw_path.strip().strip('"').strip("'")

if not os.path.exists(TEST_IMAGE_PATH):
    print(f"❌ Error: Could not find any file at '{TEST_IMAGE_PATH}'. Please check for typos and try again.")
    exit()

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Testing on device: {DEVICE}")

# 2. Load the Model
print("Loading model architecture...")
model = UNet(3, 1)

print(f"Loading trained weights from: {MODEL_WEIGHTS_PATH}")
state_dict = torch.load(MODEL_WEIGHTS_PATH, map_location=DEVICE, weights_only=True)

# Strip the "module." prefix if trained on multiple GPUs
if list(state_dict.keys())[0].startswith('module.'):
    state_dict = {k[7:]: v for k, v in state_dict.items()}

model.load_state_dict(state_dict)
model.to(DEVICE)
model.eval()
print("Model loaded successfully!")

# 3. Process the Image and Predict
print(f"Processing image: {TEST_IMAGE_PATH}")
orig_img = Image.open(TEST_IMAGE_PATH).convert("RGB")

img_array = np.array(orig_img, dtype=np.float32) / 255.0
img_tensor = torch.tensor(np.transpose(img_array, (2, 0, 1))).unsqueeze(0).to(DEVICE)

print("Generating prediction...")
with torch.no_grad():
    pred_logits = model(img_tensor)
    pred_probs = torch.sigmoid(pred_logits)
    pred_binary = (pred_probs > 0.5).float().cpu().squeeze().numpy()

# 4. Display the Results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(orig_img)
axes[0].set_title("Original Input Image", fontsize=14)
axes[0].axis('off')

axes[1].imshow(pred_binary, cmap='gray')
axes[1].set_title("U-Net Predicted Mask", fontsize=14)
axes[1].axis('off')

plt.tight_layout()
plt.show()