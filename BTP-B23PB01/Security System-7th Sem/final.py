import cv2
import torch
import numpy as np
import requests
import time
from ultralytics import YOLO

# Replace this with the path to your YOLO model
model = YOLO('yolov8n.pt')  # Adjust the confidence threshold as needed

# Define a function to process and modify the image from the camera
def process_frame():
    # Initialize the webcam
    videostream = cv2.VideoCapture(0)

    # Initialize variables for Opera_House detection count and ThinkSpeak update count
    write_api_key = "AX6SLUKWUHTO0EWT"
    url = "https://api.thingspeak.com/update"

    # Variable to track if person was detected in the last frame
    person_detected_last_frame = False

    while True:
        # Grab frame from the video stream
        ret, frame = videostream.read()

        # Make predictions with the YOLO model directly on the frame
        with torch.no_grad():
            results = model.predict(frame)

        # Get the class predictions
        class_predictions = results[0].boxes.cls.cpu().numpy()

        # Check if "person" class is present in predictions
        person_detected_current_frame = 0 in class_predictions  # Assuming "person" has class ID 0

        # Check if a person was detected in both the current and last frames
        if person_detected_last_frame and person_detected_current_frame:
            payload = {'api_key': write_api_key, 'field1': 1}  # Assuming the field is named 'field1'
            response = requests.get(url, params=payload)
            print(f"Data sent to Databse.")
            print("PERSON DETECTED IN CONSECUTIVE FRAMES")
        else:
            payload = {'api_key': write_api_key, 'field1': 0}  # Assuming the field is named 'field1'
            response = requests.get(url, params=payload)
            print(f"NO DETECTION.")

        # Update the variable for the next iteration
        person_detected_last_frame = person_detected_current_frame

        # Display the frame
        cv2.imshow('Object Detector', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

        # Sleep for 10 seconds before processing the next frame
        time.sleep(10)

    # Clean up
    cv2.destroyAllWindows()
    videostream.release()

# Process the frame from the camera
process_frame()