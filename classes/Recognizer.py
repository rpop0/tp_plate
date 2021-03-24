from cv2 import cv2
import numpy as np
import easyocr
import imutils

class Recognizer:
    def __init__(self, path):
        self.path = path

    #processes mask from input image
    def process_image(self):
        #import image from path
        img = cv2.imread(self.path)
        img = cv2.resize(img, (640, 480))

        #-------------- Proces contours --------------

        #apply filters on image
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_filter = cv2.bilateralFilter(img_gray, 13, 15, 15)
        img_edges = cv2.Canny(img_filter, 30, 200)
        
        #test for edge detection
        cv2.imshow("Test", img_edges)
        cv2.waitKey(0)

        #-------------- Mask out plate --------------
        
        #grabs contoursfrom image
        plate = cv2.findContours(img_edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(plate)
        #storestop 10 results
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

        #plate location
        loc = None

        #iterate results to find a best fit for a plate
        for cnt in contours:
            aprox = cv2.approxPolyDP(cnt, 10, True)
            #breaks if plate is found
            if len(aprox) == 4:
                loc = aprox
                break
        
        #creates new mask for the number plate
        new_mask = np.zeros(img_gray.shape, np.uint8)
        img_masked = cv2.drawContours(new_mask, [loc], 0, 255, -1)
        #applyes mask on the image
        img_masked = cv2.bitwise_and(img_gray, img_gray, mask = new_mask)

        #test for plate mask
        cv2.imshow("Test", img_masked)
        cv2.waitKey(0)

        #cuts the image to show only the maskedpart
        (x, y) = np.where(new_mask == 255)
        img_cut = img_masked[np.min(x):np.max(x) + 1, np.min(y):np.max(y) + 1]

        #test for plate mask cut
        cv2.imshow("Test", img_cut)
        cv2.waitKey(0)

        #returns processed image and number location
        return img_cut, loc

    #extracts number from masked image
    def process_number(self, img_cut, loc):
        #import image from path
        img = cv2.imread(self.path)
        img = cv2.resize(img, (640, 480))
        
        #uses easyocr to read plate (language = ro)
        read = easyocr.Reader(['ro'])
        plate_result = read.readtext(img_cut)
        
        #print text detection test
        print("\nPlate : ", plate_result[0][-2], "\nAccuracy : ", plate_result[0][-1])
        
        display_color = (0, 255, 0)

        #renders result on top of original image
        plate_number = plate_result[0][-2]
        img_result = cv2.putText(img, text = plate_number, org = (10, 60), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = display_color, thickness = 2, lineType = cv2.LINE_AA)
        img_result = cv2.rectangle(img, tuple(loc[0][0]), tuple(loc[2][0]), display_color, 3)

        #Show final image
        cv2.imshow("Test", img_result)
        cv2.waitKey(0)