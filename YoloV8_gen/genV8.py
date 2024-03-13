# This code as the goal of generating the YoloV8 .txt files for training and testing. The goal is to click on images to generate the .txt files

import sys
import numpy as np
import cv2


def open_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('image', image)
    return image

class Coordinates:
    
    def __init__(self, image):
        self.image = image
        self.height, self.width, self.channels = image.shape
        self.click_coord = []
        self.should_close = False 


    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, ' ', y)
            self.click_coord.append([x, y])
            if len(self.click_coord) == 4:
                print(self.click_coord)
                print("Middle: ", self.middle())
                self.click_coord = []  # Reset the list for next four clicks
                self.should_close = True

    def middle(self):
        height, width, _ = self.height, self.width, self.channels
        x = (self.click_coord[0][0] + self.click_coord[2][0]) / 2
        y = (self.click_coord[1][1] + self.click_coord[3][1]) / 2

        # Normalize the values
        x = x / width
        y = y / height

        print(x, ' ', y)

        return x, y

def yoloV8_txt(image, x, y):
    string = "0 f{x} f{y} " # 0 is the class human
    
def main():
    image_path = "/home/alex/salutis/business_canvas_model.png"
    image = open_image(image_path)
    coordinates = Coordinates(image)
    cv2.setMouseCallback('image', coordinates.click_event)
    
    try:
        while True:
            if coordinates.should_close:  # Check the flag to see if the window should be closed
                cv2.destroyAllWindows()
                break
            if cv2.waitKey(1) & 0xFF == 27:  # ASCII value of ESC is 27
                break
    except KeyboardInterrupt:
        print("\n Interrupted by user")

main()