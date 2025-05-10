# R3ST: A Synthetic Dataset with Real Trajectories for Urban Traffic Analysis 🚗

[![Paper on OpenReview](https://img.shields.io/badge/Paper-OpenReview-orange)](https://openreview.net/forum?id=dummy-id)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Dataset](https://img.shields.io/badge/data-Google%20Drive-brightgreen)](https://drive.google.com/drive/folders/1ibP6TcPVmAQ6X5ZrDYwL-Iu5e39mntgX?usp=sharing)
[![Website](https://img.shields.io/badge/Website-R3ST.vision-red)](https://r3st-website.vercel.app/)

## 📌 Official Repository

This is the official repository for the paper “R3ST: A Synthetic Dataset with Real Trajectories for Urban Traffic Analysis”, accepted at the SynData4CV Workshop @ CVPR 2025.

## 🚧 Repository Status

This repository is currently **under development**.  
Not all data and resources have been uploaded yet. Please check back soon for updates.

## 📝 Abstract

> Datasets are essential to train and evaluate computer vision models used for traffic analysis and to enhance road safety. Existing real datasets fit real-world scenarios, capturing authentic road object behaviors, however, they typically lack precise >ground-truth annotations. In contrast, synthetic datasets play a crucial role, allowing for the annotation of a large number of frames without additional costs or extra time. However, a general drawback of synthetic datasets is the lack of realistic >vehicle motion, since trajectories are generated using AI models or rule-based systems. In this work, we introduce **R3ST** (Realistic 3D Synthetic Trajectories), a synthetic dataset that overcomes this limitation by generating a synthetic 3D >environment and integrating real-world trajectories derived from SinD, a bird's-eye-view dataset recorded from drone footage.
> The proposed dataset closes the gap between synthetic data and realistic trajectories, advancing the research in trajectory forecasting of road vehicles, offering both accurate multimodal ground-truth annotations and authentic human-driven vehicle >trajectories.

## ⬇️ Dataset Download

You can download the R3ST dataset from the following Google Drive link:  
**[Download R3ST Dataset](https://drive.google.com/drive/folders/1ibP6TcPVmAQ6X5ZrDYwL-Iu5e39mntgX?usp=sharing)**

## 📁 Folder Structure

The Drive folder is organized as follows:

```text
R3ST/
├── README.txt                  # Overview of dataset content
├── Scene Locations/
│   ├── Camera1/
│   │   ├── frames/            # Jpeg frames
│   │   ├── labels/            # Bounding-box per-frame annotation in YOLO style
|   |   ├── npz/               # Multimodal annotations computed by Vision Blender
│   │   └── camera_info.json   # Information about the position and intrinsic matrix of the camera
│   ├── Camera2/
│   │   └── ...
```

## 🧩 Multimodal Annotations

R3ST includes segmentation masks and depth maps as part of its multimodal annotations.  
You can use the provided script to extract and visualize this data from `.npz` files.

### 🛠️ Setup

We recommend using a Conda environment:

```bash
conda create -n r3st-multimodal python=3.10
conda activate r3st-multimodal
pip install -r requirements.txt

python read_npz.py --npz path/to/file.npz --out path/to/output_dir
```

## 📚 Citation

If you use **R3ST** in your research, please cite our paper:

### BibTeX

```bibtex
@inproceedings{
          teglia2025rst,
          title={R3{ST}: A Synthetic Dataset with Real Trajectories for Urban Traffic Analysis},
          author={Simone Teglia and Claudia Melis Tonti and Francesco Pro and Leonardo Russo and Andrea Alfarano and Matteo Pentassuglia and Irene Amerini},
          booktitle={Synthetic Data for Computer Vision Workshop @ CVPR 2025},
          year={2025},
          url={https://openreview.net/forum?id=VCORXe6I5B}
          }
```
