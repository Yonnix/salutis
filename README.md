# Salutis

A YOLOv8-based computer vision project for object detection and image annotation.

## Description

Salutis is a Chitkara project that implements YOLOv8 for object detection tasks. The repository includes tools for dataset preparation, image annotation, and model training/inference.

## Features

- **YOLOv8 Annotation Tool**: Interactive image annotation system using mouse clicks to generate YOLO format training labels
- **Image Preprocessing**: Utilities to resize images to 640x640 for optimal YOLOv8 performance
- **Model Training**: Custom YOLOv8 model training capabilities
- **Inference Pipeline**: Run predictions on new images using trained models

## Project Structure

```
salutis/
├── YoloV8_gen/       # Annotation and preprocessing tools
│   ├── genV8.py      # Interactive annotation tool for generating YOLO .txt files
│   └── resize.py     # Image resizing utility
├── data/             # Training and testing datasets
├── models/           # Trained model weights
├── images/           # Input images
├── demo/             # Demo outputs
├── render/           # Visualization outputs
└── runs/             # Training runs and results
```

## Usage

### Resize Images
```bash
python YoloV8_gen/resize.py <path_to_images_folder>
```

### Generate Annotations
Use `genV8.py` to interactively annotate images by clicking four points to define bounding boxes. The tool automatically converts coordinates to YOLO format.

## License

This project is licensed under the MIT License.

## Technologies

- Python
- OpenCV
- YOLOv8
- Jupyter Notebook
