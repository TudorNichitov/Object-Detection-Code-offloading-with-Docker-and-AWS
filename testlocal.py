
import base64
# import Pillow as PIL
from PIL import Image
from PIL import ImageDraw
import os
import detect

# import tflite_runtime.interpreter as tflite UNCOMMENT FOR DOCKER EXECUTION AND COMMENT NEXT ONE
import tensorflow.lite as tflite

import platform
import datetime
import cv2
import time
import numpy as np
import io
from io import BytesIO
from flask import Flask, request, Response, jsonify, make_response
import random
import re

MODEL_PATH = "models/mobilenet_ssd_v2_coco_quant_postprocess.tflite"
CONFIDENCE_TH = 0.2

#app = Flask(__name__)


# THIS FILE IS INTENTED FOR TESTING THE APP LOCALLY


# Get a bunch of images as 64 bit encoded strings, loaded locally
class DetectionObject:
    def __init__(self, class_id, confidence, bouning_box):
        self.class_id = class_id
        self.confidence = confidence
        self.bouning_box = bouning_box
# Update the detection loop so it gets the array of strings (images)

def detection_loop(detector, confidence_th, images):
    # the output = a dict with this format:
    """
         data = {
             "status": 200,
             "bounding_boxes": bounding_boxes,
             "inf_time": inf_times,
             "avg_inf_time": str(avg_inf_time),
             "upload_time": upload_times,
             "avg_upload_time": str(avg_upload_time)
         }
    """


    #array of dictionaries with the specified format
    data = []

    for image in images:

        # extract image from image array - image is as a base 64 string

        #run_detector on the image
        obj, inference_time = detect.run_detector(detector, CONFIDENCE_TH, image)

        entry = {
            "status": 200,
            "bounding_boxes": obj.bouning_box,
            "inf_time": inference_time,
             #"avg_inf_time": str(avg_inf_time),
             #"upload_time": upload_times[i],
             #"avg_upload_time": str(avg_upload_time)
             }

        data.append(entry) #the array of dictionaries containing the bounding boxes and inf time

    # Calculate average inference time and Add it to each element in dict
    total_inf_time = 0.0
    num_entries = len(data)
    for entry in data:
        inf_time = entry["inf_time"]

        # add them up
        total_inf_time += inf_time


    avg_inf_time = total_inf_time / num_entries

    # Update the average inference time in the current dictionary
    for entry in data:
        entry["avg_inf_time"] = avg_inf_time

    #return data
    return make_response(jsonify(data), 200)


#load the images from local folder into array of strings
image_folder = "data/object-detection-tiny"
image_files = os.listdir(image_folder)

image_base64_list = []

for image_file in image_files:
     image_path = os.path.join(image_folder, image_file)
     with open(image_path, 'rb') as f:
         image_data = f.read()
         image_base64 = base64.b64encode(image_data).decode('utf-8')
         image_base64_list.append(image_base64)

image_array = np.array(image_base64_list)

# initializing the flask app
app = Flask(__name__)

#test output of local files
if __name__ == "__main__":
    # test_detector:


    detector = tflite.Interpreter(model_path=MODEL_PATH)
    detector.allocate_tensors()

    data = detection_loop(detector, CONFIDENCE_TH, image_array)
    print(data)