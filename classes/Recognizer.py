from cv2 import cv2
import numpy as np
import imutils

class Recognizer:
    def __init__(self, path):
        self.path = path

    def show(self):
        img = cv2.imread(self.path)
        cv2.imshow("Test", img)
        cv2.waitKey(0)

    def process_image(self):
        img = cv2.imread(self.path)
        img = cv2.resize(img, (640, 480))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bilateralFilter(img, 13, 15, 15)
        img = cv2.Canny(img, 30, 200)
        