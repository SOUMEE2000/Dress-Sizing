import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose
pose_image = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

import math

def calc_shoulder_dist(lst, len_x, len_y):
  x = int(lst[11].x*len_x)
  y = int(lst[11].y*len_y)

  x2 = int(lst[12].x*len_x)
  y2 = int(lst[12].y*len_y)
  dist = math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2))
  return dist

def detectPose(image_pose,image_target_pose, pose, draw=False, display=False):
    
    original_image = image_pose.copy()
    
    image_in_RGB = cv2.cvtColor(image_target_pose, cv2.COLOR_BGR2RGB)
    resultant = pose.process(image_in_RGB)
    len_x = image_in_RGB.shape[1]
    len_y = image_in_RGB.shape[0]
    img_target_length = calc_shoulder_dist(resultant.pose_landmarks.landmark,len_x, len_y)

    image_in_RGB = cv2.cvtColor(image_pose, cv2.COLOR_BGR2RGB)
    resultant = pose.process(image_in_RGB)
    len_x = image_in_RGB.shape[1]
    len_y = image_in_RGB.shape[0]
    img_length = calc_shoulder_dist(resultant.pose_landmarks.landmark,len_x, len_y)

    if resultant.pose_landmarks and draw:    
        print(type(resultant), resultant.pose_landmarks.landmark[0])
        mp_drawing.draw_landmarks(image=original_image, landmark_list=resultant.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  #connections=frozenset({(11,12),(24,26),(23,25),(11,13),(12,14),(13,15),(14,16),(26,28),(25,27)}),
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255), thickness=3, circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237), thickness=2, circle_radius=2))
        
    if display:
        
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image_pose[:,:,::-1]);plt.title("Input Image");plt.axis('off');
        plt.subplot(122);plt.imshow(original_image[:,:,::-1]);plt.title("Pose detected Image");plt.axis('off');
        return int(img_target_length-img_length)*10

    else:
      return original_image
