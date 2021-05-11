from cv2 import cv2
import easyocr
import numpy as np


def ocr_images(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(img, 13, 15, 15)
    img = cv2.Canny(img, 80, 150)
    reader = easyocr.Reader(['ro'])
    plate = reader.readtext(img)[0][-2]
    print(f"\nRecognized license plate: {plate}")
