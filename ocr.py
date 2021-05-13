from cv2 import cv2
import pytesseract
from PIL import Image


def ocr_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 3)
    cv2.imwrite(path, img)

    txt = pytesseract.image_to_string(Image.open(path))
    print()
    print(txt)
    print()
