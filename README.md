# Object Detection Application with Docker, Python, and TensorFlow

This project explores the implementation of an object detection application using Docker, Python, and TensorFlow. The performance differences between local and remote execution on AWS are analyzed, considering metrics such as inference time and transfer time. Insights into the conditions favoring data offloading are provided.

## Overview
The project involves:
- Object detection on various image collections.
- Dockerizing the application and sending requests via POST.
- Deploying the application locally and remotely on AWS, collecting transfer and inference times.
- Evaluating deployment decisions based on resource usage and time consumption.

## Problem Overview
### Tasks
The project utilizes three datasets (BIG, MEDIUM, SMALL) with varying numbers of JPG images. Images range from 14 KB to 495 KB, encoded in RGB, and compressed using lossy JPEG compression.

## Methodology and Approach
### Model
The application employs a pretrained model, Mobilenet SSD V2, optimized for fast object detection on mobile devices.

### Object Detection App
The Flask application ('app.py') exposes an API endpoint for object detection. The application decodes base64 images, processes them, and returns results including class ID, bounding boxes, and inference times.

### Dockerization
Docker is used to create a portable and independent container for the application. Docker containers are deployed locally and remotely, facilitating scalability.

### Metrics
Inference and upload times are measured for each input. Average times are calculated for evaluation.

### Experimental Setup
Local execution is performed on an Ubuntu machine with 12 CPU cores and 16 GB RAM. Remote execution is on an AWS EC2 instance with 2 CPU cores and 8 GB RAM.

### Results and Conclusions - See Report