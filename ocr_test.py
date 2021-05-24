import ocr
from cv2 import cv2

def main():
    rec = cv2.imread("./S11.jpg")

    ocr.extract_plate_text(rec)

    cv2.imshow("Result", rec)
    cv2.waitKey(0)
    cv2.destroyAllWindows


if __name__ == "__main__":
    main()