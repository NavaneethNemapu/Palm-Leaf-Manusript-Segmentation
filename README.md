# Palm Leaf Manuscript Segmentation (PLM-SegNet)

This repository contains the code and resources for a Deep Learning-based image segmentation project focused on **Palm Leaf Manuscripts**. The primary goal is to accurately segment and extract text and structural features from ancient, degraded palm leaf manuscripts using a customized U-Net architecture.

## Project Overview

Palm leaf manuscripts are invaluable historical documents that suffer from degradation over time. This project utilizes an advanced image segmentation model (**PLM-SegNet**, based on the U-Net architecture) to distinguish the engraved or handwritten text from the noisy, textured background of the palm leaves. 

### Key Highlights
- **Architecture**: U-Net based Convolutional Neural Network (CNN) tailored for document image segmentation.
- **Dataset**: Trained on a large-scale dataset of 12,000 palm leaf images and their corresponding ground truth segmentation masks.
- **Metrics**: Evaluated using industry-standard segmentation metrics including Dice Coefficient, Intersection over Union (IoU), and a custom Combined Loss function to handle severe class imbalances and noise.

## Repository Structure

- `requirements.txt`: Python dependencies required to run the project.
- `palm-leaf-segmentation-code.ipynb`: The main Jupyter Notebook containing the training pipeline, model definition, and data preprocessing steps.
- `Palm_Leaf_Segmentation_Report.pdf`: A comprehensive 4-page technical report detailing the methodology, system architecture, dataset, and training results over 50 epochs.
- `best_model.pth`: (Local only) The saved PyTorch model weights after training.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NavaneethNemapu/Palm-Leaf-Manusript-Segmentation.git
   cd Palm-Leaf-Manusript-Segmentation
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   # On Windows
   .\env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure you have PyTorch installed with the appropriate CUDA version if running on a GPU).*

## Usage

### Training
To train the model from scratch or explore the training pipeline, open the Jupyter Notebook:
```bash
jupyter notebook palm-leaf-segmentation-code.ipynb
```

### Inference
Ensure you have the `best_model.pth` file downloaded and placed in the project root directory. Inference can be run by loading the PyTorch model and passing an image tensor through it, as demonstrated in the notebook.

## Results
After training, the model successfully learned to isolate textual elements from heavily textured and degraded palm leaf backgrounds with exceptional accuracy. 

### Final Evaluation Metrics
- **Mean Intersection over Union (IoU):** 0.9826 (98.26%)
- **Dice Coefficient:** 0.9912 (99.12%)
- **Validation Loss:** 0.0365

Detailed loss graphs, performance metrics, and sample predictions can be found in the included technical report.

## License
This project is open-source and available for educational and research purposes.
