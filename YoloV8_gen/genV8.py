# This code as the goal of generating the YoloV8 .txt files for training and testing. The goal is to click on images to generate the .txt files

import sys
import numpy as np
import cv2
import os



def open_images(image_folder_path):
    for image in os.listdir(image_folder_path):
        image_path = os.path.join(image_folder_path, image)
        img = cv2.imread(image_path)
        yield image_path ,img 
        while True:
            k = cv2.waitKey(0) & 0xFF
            if k == ord(' '):  # space key
                break

class Coordinates:
    
    def __init__(self, image, file_name):
        self.image = image
        self.height, self.width, self.channels = image.shape
        self.click_coord = []
        self.string = ""
        self.file_name = file_name
        # self.should_close = False 


    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, ' ', y)
            self.click_coord.append([x, y])
            if len(self.click_coord) == 4:
                print(self.click_coord)
                print("Middle: ", self.middle())
                print("Height and Width: ", self.hight_width())
                self.yoloV8_txt()
                self.click_coord = []  # Reset the list for next four clicks
                # self.should_close = True


    def middle(self):
        height, width, _ = self.height, self.width, self.channels
        X = (self.click_coord[0][0] + self.click_coord[2][0]) / 2
        Y = (self.click_coord[1][1] + self.click_coord[3][1]) / 2

        # Normalize the values
        X = X / width
        Y = Y / height

        return X, Y
    

    def hight_width(self):
        height, width, _ = self.height, self.width, self.channels
        h = self.click_coord[3][1] - self.click_coord[1][1] # Second and fourth click
        w = self.click_coord[2][0] - self.click_coord[0][0] # First and third click

        # Normalize the values
        h = h / height
        w = w / width

        return h, w
    

    def yoloV8_txt(self):
        X, Y = Coordinates.middle(self)
        h, w = Coordinates.hight_width(self)
        self.string = "0 " + str(X) + " " + str(Y) + " " + str(h) + " " + str(w) + "\n"
        with open(self.file_name + ".txt", "a") as file:
            file.write(self.string)
    

def main():
    images_path = sys.argv[1] # Path in the command line to the images
    images = open_images(images_path)
    # for image in images:
    #     cv2.imshow("test", image)
    try:
        for image_name, image in images:
            # Create .txt file with the same name as the image
            file_name = image_name.split("/")[-1].split(".jpg")[0] + ".txt"
            print(file_name)
            cv2.imshow('image', image)
            coordinates = Coordinates(image, file_name)
            is_closed = False
            while not is_closed:
                cv2.imshow('image', image)
                cv2.setMouseCallback('image', coordinates.click_event)
                k = cv2.waitKey(1) & 0xFF  # Non-blocking key check
                if k == ord(' '):  # space key
                    is_closed = True
            cv2.waitKey(1)  # Ensure the window is destroyed before the next image is displayed
    except KeyboardInterrupt:
        print("\n Interrupted by user")

main()