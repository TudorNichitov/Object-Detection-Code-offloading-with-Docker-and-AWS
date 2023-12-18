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

## Results
Local execution consistently outperforms remote execution in terms of inference time and overall time, as shown in Figure 1. Table 1 presents average values, reinforcing the superiority of local execution. The experiment highlights the limited advantage of remote deployment in this specific context.

![Results](img/results.png)

*Figure 1: Performance comparison between local and remote execution.*

## Conclusions

### Is it worth offloading execution on the remote cluster? If not, why?
Based on our experiments, offloading execution to a remote cluster did not provide benefits in our case. It not only increased execution time but also introduced complexity and dependencies on factors like internet stability, workload availability, and AWS costs. Additionally, keeping data locally enhances privacy, especially when dealing with sensitive images. The limited compute power on AWS hindered performance, with upload times comprising a significant portion of the overall time. With faster remote computing power, the outcome might have been different.

### What would be needed to improve the performance of remote and local execution?
Our comparison highlights two key factors influencing cloud computing results: computing power and upload time. Improving computing power on AWS and reducing upload time (via higher bandwidth or better data compression) could significantly enhance the appeal of offloading computationally intensive tasks.

### Can you think of a scenario where offloading improves performance?
While offloading did not prove beneficial for our specific task, numerous scenarios exist where offloading is not only useful but essential. For instance, in setups with a single sensor connected to a weak microcomputer, external computing capabilities become crucial. Additionally, as 5G adoption increases, higher transmission speeds may make offloading more advantageous in the future.

---

*Note: For detailed instructions, code, and additional findings, please refer to the project files and complete report.*
