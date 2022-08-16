import cv2
import numpy as np

def update_nose_position(width, position, background, img, video_capture):
    aspect_ratio = img.shape[1] / img.shape[0]
    height = int(width/aspect_ratio)
    if position[0] <= 0 or position[1] <= 0 or position[0]+width >= len(video_capture[0]) or position[1]+height >= len(video_capture):
        return
    resize_img = cv2.resize(img, (width, height))
    gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
    nose_area = background[position[1]: position[1]+height, position[0]: position[0]+width]
    nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask = mask)
    final_nose = cv2.add(nose_area_no_nose, resize_img)
    background[position[1]: position[1]+height, position[0]: position[0]+width] = final_nose
