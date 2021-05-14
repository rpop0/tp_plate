from cv2 import cv2
import pytesseract
from PIL import Image

def ocr_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    img = cv2.medianBlur(img, 3)
    cv2.imwrite(path, img)

    new_img = Image.open(path)
    txt = pytesseract.image_to_string(new_img)
    print()
    print(txt)
    print()
