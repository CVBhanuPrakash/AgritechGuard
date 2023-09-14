from ultralytics import YOLO
import cv2
import time

# load yolov8 model
model = YOLO('yolov8n.pt')
# load video
# video_path = './test.mp4'
# video_path = './Cctv capture thief stealing children.mp4'
video_path = './Elephant Attacking house...mp4'
# cap = cv2.VideoCapture(video_path)
cap = cv2.VideoCapture(0)

# Set the desired interval (in seconds) for object detection
detection_interval = 5  # Change this to your preferred interval

# Initialize variables for object tracking
tracker = None
object_detected = False

last_detection_time = time.time()

ret = True
# read frames
while ret:
    ret, frame = cap.read()

    if ret:

        current_time = time.time()

        # Check if it's time to perform object detection
        if current_time - last_detection_time >= detection_interval:

            # Reset the last detection time
            last_detection_time = current_time

            # Detect objects
            results = model.track(frame, persist=True)

            # ...

            # if results and len(results.pred[0]) > 0:
            #     # Get the bounding box coordinates in (x_center, y_center, width, height) format
            #     bbox = results.pred[0][:, :4].cpu().numpy()
            #
            #     if tracker is None:
            #         # Initialize the object tracker
            #         tracker = cv2.TrackerCSRT_create()
            #         # Convert the bbox to (x, y, width, height) format
            #         bbox = (bbox[0] - bbox[2] / 2, bbox[1] - bbox[3] / 2, bbox[2], bbox[3])
            #         tracker.init(frame, tuple(bbox))
            #
            # # ...

            # Plot results
            frame_ = results[0].plot()

            # Visualize
            # cv2.imshow('frame', frame_)

        # Show alert if an object is detected
        if object_detected:
            print("Object detected")
            object_detected = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# from ultralytics import YOLO
# import cv2
# import time
#
# # load yolov8 model
# model = YOLO('yolov8n.pt')
# # load video
# # video_path = './test.mp4'
# # video_path = './Cctv capture thief stealing children.mp4'
# video_path = './Elephant Attacking house...mp4'
# # cap = cv2.VideoCapture(video_path)
# cap = cv2.VideoCapture(0)
#
# # Set the desired interval (in seconds) for object detection
# detection_interval = 5  # Change this to your preferred interval
#
# # Initialize variables for object tracking
# tracker = None
# object_detected = False
#
# last_detection_time = time.time()
#
# ret = True
# # read frames
# while ret:
#     ret, frame = cap.read()
#
#     if ret:
#
#         current_time = time.time()
#
#         # Check if it's time to perform object detection
#         if current_time - last_detection_time >= detection_interval:
#             # Reset the last detection time
#             last_detection_time = current_time
#
#             # Detect objects
#             results = model.track(frame, persist=True)
#
#             # ...
#
#             # if results and len(results.pred[0]) > 0:
#             #     # Get the bounding box coordinates in (x_center, y_center, width, height) format
#             #     bbox = results.pred[0][:, :4].cpu().numpy()
#             #
#             #     if tracker is None:
#             #         # Initialize the object tracker
#             #         tracker = cv2.TrackerCSRT_create()
#             #         # Convert the bbox to (x, y, width, height) format
#             #         bbox = (bbox[0] - bbox[2] / 2, bbox[1] - bbox[3] / 2, bbox[2], bbox[3])
#             #         tracker.init(frame, tuple(bbox))
#             #
#             # # ...
#
#             # Plot results
#             frame_ = results[0].plot()
#
#             # Visualize
#             cv2.imshow('frame', frame_)
#
#         # Show alert if an object is detected
#         if object_detected:
#             print("Object detected")
#             object_detected = False
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

