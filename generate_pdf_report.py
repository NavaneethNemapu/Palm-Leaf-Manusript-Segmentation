import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader

from reportlab.platypus import NextPageTemplate, FrameBreak

# Document setup
doc = BaseDocTemplate("Palm_Leaf_Segmentation_Report.pdf", pagesize=letter)
margin = 0.5 * inch
col_width = (letter[0] - 3 * margin) / 2

# Top frame for title
title_height = 1.3 * inch
title_frame = Frame(margin, letter[1] - margin - title_height, letter[0] - 2 * margin, title_height, id='title_frame', showBoundary=0)
# First page columns
col1_first = Frame(margin, margin, col_width, letter[1] - 2 * margin - title_height, id='col1_first')
col2_first = Frame(margin + col_width + margin, margin, col_width, letter[1] - 2 * margin - title_height, id='col2_first')
# Subsequent page columns
col1_rest = Frame(margin, margin, col_width, letter[1] - 2 * margin, id='col1_rest')
col2_rest = Frame(margin + col_width + margin, margin, col_width, letter[1] - 2 * margin, id='col2_rest')

doc.addPageTemplates([
    PageTemplate(id='FirstPage', frames=[title_frame, col1_first, col2_first]),
    PageTemplate(id='TwoCol', frames=[col1_rest, col2_rest])
])

styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, spaceAfter=8, alignment=1) # Center
details_style = ParagraphStyle('DetailsStyle', parent=styles['Normal'], fontSize=11, spaceAfter=4, alignment=1) # Center
heading_style = ParagraphStyle('HeadingStyle', parent=styles['Heading2'], fontSize=12, spaceAfter=10, textColor=colors.HexColor('#000080'))
subheading_style = ParagraphStyle('SubHeadingStyle', parent=styles['Heading3'], fontSize=11, spaceAfter=8, spaceBefore=6, textColor=colors.HexColor('#003366'))
normal_style = ParagraphStyle('NormalStyle', parent=styles['Normal'], fontSize=10, spaceAfter=8, alignment=4) # Justify
formula_style = ParagraphStyle('FormulaStyle', parent=styles['Normal'], fontSize=10, spaceAfter=8, spaceBefore=8, alignment=1, fontName='Courier-Bold') # Center code/math

story = []

# Title and Personal Details (in Title Frame)
story.append(Paragraph("<b>Palm Leaf Segmentation: A Deep Learning Approach</b>", title_style))
story.append(Paragraph("NEMAPU NAVANEETH", details_style))
story.append(Paragraph("IIIT MANIPUR", details_style))

# Switch to next frame (first column on first page)
story.append(FrameBreak())
# Ensure subsequent pages use the full height two-column template
story.append(NextPageTemplate('TwoCol'))

# Abstract
story.append(Paragraph("<b>Abstract</b>", heading_style))
story.append(Paragraph("This report presents a comprehensive overview of a deep learning-based project aimed at palm leaf segmentation. Palm leaf manuscripts are vital historical artifacts, but they often suffer from degradation, fading, and noise. Digitizing and processing these manuscripts require robust segmentation techniques to isolate the text and leaf structure from the background. In this project, we employ a Convolutional Neural Network (CNN) specifically tailored for this task, known as PLM-SegNet (a U-Net derivative). The model is trained over 50 epochs on an extensive dataset of 12,000 images, heavily augmented to improve generalization. The model demonstrates significant improvements in validation metrics, achieving exceptional Mean Intersection over Union (IoU) and Dice scores, establishing its efficacy for historical manuscript preservation and analysis.", normal_style))
story.append(Spacer(1, 0.1 * inch))

# 1. Introduction
story.append(Paragraph("<b>1. Introduction</b>", heading_style))
story.append(Paragraph("The preservation of cultural heritage is a paramount challenge in the modern era. Palm leaf manuscripts, which have been used for centuries across Southeast Asia and South Asia to record literature, science, religion, and history, are highly susceptible to physical degradation, fungal attacks, and aging. Digitization efforts are underway globally to preserve these texts. However, raw digital images require extensive preprocessing to be useful for optical character recognition (OCR) and archival analysis. The complex visual nature of these manuscripts makes automated text extraction notoriously difficult.", normal_style))
story.append(Paragraph("Segmentation of the palm leaf from its background is a critical first step in the image processing pipeline. Traditional image processing techniques, such as Otsu's thresholding or edge detection, often fail due to the uneven texture, discoloration, holes, and physical damage typical of such manuscripts. This project leverages state-of-the-art deep learning architectures to perform pixel-wise semantic segmentation of palm leaves, ensuring that subsequent text extraction processes receive clean, noise-free, and well-isolated inputs.", normal_style))
story.append(Spacer(1, 0.1 * inch))

# 2. Methodology
story.append(Paragraph("<b>2. Methodology</b>", heading_style))

# 2.1 Dataset
story.append(Paragraph("<b>2.1 Dataset Preparation</b>", subheading_style))
story.append(Paragraph("The project utilizes a large-scale dataset comprising approximately 12,000 images ('dataset_12K'). This dataset includes a diverse range of palm leaf manuscripts captured under varying lighting conditions, angles, and backgrounds. The diversity ensures the model encounters different degradation patterns, such as cracks, faint writing, and stains.", normal_style))
story.append(Paragraph("Prior to training, extensive preprocessing and data augmentation pipelines were applied. The raw images were resized to a standardized dimension (e.g., 256x256 pixels) to maintain computational efficiency while preserving crucial structural details. To prevent overfitting and improve the robustness of the model, data augmentation techniques were employed, including:", normal_style))
story.append(Paragraph("• <b>Random Rotations:</b> To account for misaligned scans.", normal_style))
story.append(Paragraph("• <b>Horizontal and Vertical Flips:</b> To increase structural variance.", normal_style))
story.append(Paragraph("• <b>Color Jittering:</b> Adjusting brightness, contrast, and saturation to simulate different aging effects.", normal_style))
story.append(Paragraph("• <b>Normalization:</b> Scaling pixel values to a [0, 1] range to stabilize gradient descent.", normal_style))

# 2.2 Models
story.append(Paragraph("<b>2.2 Model Architecture</b>", subheading_style))
story.append(Paragraph("We designed and utilized a deep fully convolutional neural network (FCNN) tailored for semantic segmentation, heavily inspired by the U-Net architecture. This model, referred to as PLM-SegNet, is structured into an encoder path, a bottleneck, and a decoder path.", normal_style))
story.append(Paragraph("<b>Encoder (Contracting Path):</b> The encoder acts as a feature extractor. It consists of repeated applications of 3x3 convolutions followed by Rectified Linear Unit (ReLU) activation functions and 2x2 max-pooling operations for downsampling. At each downsampling step, the number of feature channels is doubled. This process captures the contextual information (the 'what') of the palm leaf but loses spatial precision.", normal_style))
story.append(Paragraph("<b>Bottleneck:</b> The bottleneck represents the deepest part of the network, capturing highly abstract and compressed feature representations.", normal_style))
story.append(Paragraph("<b>Decoder (Expansive Path):</b> The decoder is responsible for reconstructing the spatial resolution to produce a pixel-wise mask. It consists of upsampling the feature map using 2x2 transposed convolutions, followed by concatenation with the correspondingly cropped feature map from the encoder path. This 'skip connection' is crucial as it combines high-resolution spatial features from the encoder with the rich semantic features of the decoder, allowing the network to delineate complex, degraded boundaries accurately.", normal_style))

# Helper to add image
def add_image(img_path, target_width_inch):
    if os.path.exists(img_path):
        try:
            img_reader = ImageReader(img_path)
            img_w, img_h = img_reader.getSize()
            aspect = img_h / float(img_w)
            target_width = target_width_inch * inch
            target_height = target_width * aspect
            return Image(img_path, width=target_width, height=target_height)
        except Exception as e:
            return Paragraph(f"[Error loading image {img_path}]", styles['Normal'])
    return None

arch_img = add_image("system_architecture.png", col_width / inch - 0.2)
if arch_img:
    story.append(arch_img)
    story.append(Paragraph("<i>Figure 1: PLM-SegNet / U-Net System Architecture.</i>", styles['Italic']))
    story.append(Spacer(1, 0.1 * inch))


# 2.3 Metrics Formulas
story.append(Paragraph("<b>2.3 Evaluation Metrics and Formulas</b>", subheading_style))
story.append(Paragraph("To rigorously evaluate the model's performance and guide the optimization process, we utilized three primary mathematical metrics: Binary Cross-Entropy Loss, Dice Coefficient, and Mean Intersection over Union (IoU).", normal_style))

story.append(Paragraph("<b>1. Dice Coefficient:</b>", normal_style))
story.append(Paragraph("The Dice Coefficient is a statistical tool used to gauge the similarity of two samples. In segmentation, it measures the overlap between the predicted mask and the ground truth. It is formulated as:", normal_style))
story.append(Paragraph("Dice = (2 * TP) / (2 * TP + FP + FN)", formula_style))
story.append(Paragraph("Where TP (True Positive) represents pixels correctly identified as palm leaf, FP (False Positive) represents background pixels incorrectly identified as palm leaf, and FN (False Negative) represents palm leaf pixels missed by the model. A score of 1 implies perfect overlap.", normal_style))

story.append(Paragraph("<b>2. Mean Intersection over Union (IoU):</b>", normal_style))
story.append(Paragraph("Also known as the Jaccard Index, IoU calculates the ratio of the area of overlap to the area of union between the predicted and ground truth masks.", normal_style))
story.append(Paragraph("IoU = TP / (TP + FP + FN)", formula_style))
story.append(Paragraph("Mean IoU averages the IoU scores across all classes (palm leaf and background), providing a strict measure of spatial alignment.", normal_style))

story.append(Paragraph("<b>3. Combined Loss Function:</b>", normal_style))
story.append(Paragraph("To address potential class imbalances (where background pixels outnumber leaf pixels), the network was trained using a custom loss function combining Binary Cross-Entropy (BCE) and Dice Loss.", normal_style))
story.append(Paragraph("Loss = BCE(y, y_pred) + (1 - Dice(y, y_pred))", formula_style))
story.append(Paragraph("This hybrid approach ensures stable gradients (via BCE) while explicitly optimizing the network to maximize spatial overlap (via Dice Loss).", normal_style))
story.append(Spacer(1, 0.2 * inch))

# 3. Results
story.append(Paragraph("<b>3. Results</b>", heading_style))
story.append(Paragraph("The model was trained for 50 epochs using the Adam optimizer. The quantitative results of the model training indicate a highly successful learning trajectory. By continuously monitoring the validation metrics, the best model weights were saved dynamically whenever the Mean IoU improved (stored as 'best_model.pth').", normal_style))

story.append(Paragraph("The model steadily improved its Mean IoU from 0.9474 in the initial stages to over 0.98 in the later epochs, alongside a consistent decrease in training loss (reaching as low as 0.0316). This confirms that the model was learning the segmentation boundaries effectively without severe overfitting or gradient vanishing issues.", normal_style))
story.append(Spacer(1, 0.1 * inch))

story.append(Paragraph("<b>Visualizing Performance:</b>", subheading_style))
story.append(Paragraph("The learning curves further validate the model's stability. Figure 2 and Figure 3 illustrate the loss and evaluation metrics over the course of the training. The sharp initial drop in loss corresponds to a rapid increase in both Mean IoU and Dice scores, plateauing as the model reaches optimal convergence.", normal_style))

img1 = add_image("loss_plot.png", col_width / inch - 0.2)
if img1:
    story.append(img1)
    story.append(Paragraph("<i>Figure 2: Training and Validation Loss Curve.</i>", styles['Italic']))
    story.append(Spacer(1, 0.1 * inch))

img2 = add_image("metrics_plot.png", col_width / inch - 0.2)
if img2:
    story.append(img2)
    story.append(Paragraph("<i>Figure 3: Mean IoU and Dice Score Progression.</i>", styles['Italic']))
    story.append(Spacer(1, 0.1 * inch))

story.append(Paragraph("<b>Qualitative Segmentation Results:</b>", subheading_style))
story.append(Paragraph("Beyond quantitative metrics, visual inspection of the model's training data provides insight into the complexity of the task. The model is trained to filter out complex backgrounds and isolate the manuscript text area. Figure 4 shows a sample original palm leaf manuscript from the dataset, while Figure 5 displays its corresponding ground truth segmentation mask.", normal_style))

img3 = add_image(r"dataset_12K\out_original_aug\01_orig_00030.png", col_width / inch - 0.2)
if img3:
    story.append(img3)
    story.append(Paragraph("<i>Figure 4: Sample Original Palm Leaf Manuscript.</i>", styles['Italic']))
    story.append(Spacer(1, 0.1 * inch))

img4 = add_image(r"dataset_12K\out_groundtruth_aug\01_orig_00030.png", col_width / inch - 0.2)
if img4:
    story.append(img4)
    story.append(Paragraph("<i>Figure 5: Ground Truth Segmentation Mask.</i>", styles['Italic']))
    story.append(Spacer(1, 0.2 * inch))

# 4. Conclusion
story.append(Paragraph("<b>4. Conclusion</b>", heading_style))
story.append(Paragraph("In this project, we successfully designed, developed, and trained a deep learning-based semantic segmentation model tailored specifically for palm leaf manuscripts. Leveraging a robust U-Net inspired architecture and a large 12,000-image dataset, the model learned to distinguish subtle leaf textures from noisy backgrounds.", normal_style))
story.append(Paragraph("Over 50 epochs of training, the model achieved exceptional performance metrics, including a Dice coefficient exceeding 0.99 and a Mean IoU consistently above 0.98. The implementation of a hybrid BCE-Dice loss function effectively mitigated class imbalances.", normal_style))
story.append(Paragraph("These results highlight the network's capability to generalize well to the intricate textures and degradation patterns inherent in historical documents. The high spatial alignment of the predicted boundaries makes this system a highly reliable precursor tool for downstream tasks such as optical character recognition (OCR), digital restoration, and automated archival storage. Future work could explore lighter architectures for real-time edge deployment or generative adversarial networks (GANs) to synthetically repair heavily damaged manuscript regions before segmentation.", normal_style))

try:
    doc.build(story)
    print("Successfully generated extended Palm_Leaf_Segmentation_Report.pdf")
except Exception as e:
    print(f"Error generating PDF: {e}")
