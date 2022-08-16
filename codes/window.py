import cv2
import numpy as np
import os, os.path


class Window:
    
    background_width = 2000
    background_height = 1000

    arrow_width = 50
    arrow_height = 50
    
    camera_button_width = 60
    camera_button_height = 60

    ear_selected = 0
    nose_selected = 0

    def __init__(self, background):
        self.background = background
        self.background = cv2.resize(self.background,(self.background_width,self.background_height))
        
        camera_button = cv2.imread("../images/others/camera_button.jpg")
        
        camera_button = cv2.resize(camera_button, (self.camera_button_width, self.camera_button_height))

        self.spawn_arrows((700, 50), (900, 50))
        self.spawn_arrows((700, 150), (900, 150))
        self.spawn_camera_button(camera_button, (300, 600))
    
    def show(self, title, video_capture):
        self.video_capture = video_capture
        self.background[0:len(video_capture), 0:len(video_capture[0])] = video_capture
        cv2.imshow(title, self.background)

    def spawn_arrows(self, left_pos, right_pos):         
        left_arrow = cv2.imread("../images/others/left_arrow.png")
        left_arrow = cv2.resize(left_arrow,(self.arrow_width,self.arrow_height)) 
        right_arrow = cv2.imread("../images/others/right_arrow.png") 
        right_arrow = cv2.resize(right_arrow,(self.arrow_width,self.arrow_height))
        folder_icon = cv2.imread("../images/others/folder_icon.png")
        folder_icon = cv2.resize(folder_icon,(self.arrow_width,self.arrow_height)) 
        self.background[left_pos[1]:left_pos[1]+len(left_arrow), left_pos[0]:left_pos[0]+len(left_arrow[0])] = left_arrow
        self.background[right_pos[1]:right_pos[1]+len(right_arrow), right_pos[0]:right_pos[0]+len(right_arrow[0])] = right_arrow
        self.background[right_pos[1]:right_pos[1]+len(folder_icon), right_pos[0]+len(right_arrow[0])+50:right_pos[0]+len(right_arrow[0])+len(folder_icon[0])+50] = folder_icon
                
    def spawn_camera_button(self, icon, pos):
        self.background[pos[1]:pos[1]+len(icon), pos[0]:pos[0]+len(icon[0])] = icon
    
    def test(self,event,x,y,flags,param): 
        if event == cv2.EVENT_LBUTTONDOWN:
            if y >= 50 and y <= 100:
                if x >= 700 and x <= 750 and self.ear_selected > 0:
                    self.ear_selected = self.ear_selected-1
                elif x >= 900 and x <= 950 and self.ear_selected < len(os.listdir("../images/ears"))-1:
                    self.ear_selected = self.ear_selected+1
                elif x >= 1000 and x <= 1050:
                    os.startfile(os.path.realpath("../images/ears"))
            elif y >= 150 and y <= 200:
                if x >= 700 and x <= 750 and self.nose_selected > 0:
                    self.nose_selected = self.nose_selected-1
                elif x >= 900 and x <= 950 and self.nose_selected < len(os.listdir("../images/noses"))-1:
                    self.nose_selected = self.nose_selected+1
                elif x >= 1000 and x <= 1050:
                    os.startfile(os.path.realpath("../images/noses"))
            elif y >= 600 and y <= 660 and x >= 300 and x <= 360:
                cv2.imwrite("../photos/photo"+str(len(os.listdir("../photos")))+".jpg", self.video_capture)
                

