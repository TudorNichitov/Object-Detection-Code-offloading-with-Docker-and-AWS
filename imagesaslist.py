import os
import base64
import numpy as np

# Get the images in the obj detection tiny folder and convert them into a base 64 string, then append them to an array, to simulate the input from the POST request

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

#test
for image_64 in image_array:
    print(image_64)
