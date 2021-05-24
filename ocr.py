from cv2 import cv2
import pytesseract
from PIL import Image
import os
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def processAlpha(chr):
    if chr.isalpha() == False:
        if chr == '8':
            return 'B'
        elif chr == '5':
            return 'S'
        elif chr == '3':
            return 'E'
        elif chr == '7':
            return 'Z'
        elif chr == '1':
            return 'T'
    else:
        return chr

def processNumber(chr):
    if chr.isnumeric() == False:
        if chr == 'B':
            return '8'
        elif chr == 'S':
            return '5'
        elif chr == 'E':
            return '3'
        elif chr == 'Z':
            return '7'
        elif chr == 'T' or chr == 'I':
            return '1'
    else:
        return chr

def process_plate_text(text):
    initial_list = list(text)
    result_list = []

    #converts text to list
    for element in initial_list:
        if (element.isalpha() == False) and (element.isnumeric() == False):
            initial_list.remove(element)
    
    #correction for reading the RO on the plate
    if len(initial_list) > 8:
        initial_list = initial_list[2:]
        
        while len(initial_list) > 8:
            initial_list.pop()

    #print(initial_list, " -> ", len(initial_list))
    if len(initial_list) == 7:
        #only Bucharest may have 6 characters
        result_list.append('B')

        result_list.append(' ')

        #numbers
        result_list.append(processNumber(initial_list[1]))
        result_list.append(processNumber(initial_list[2]))

        result_list.append(' ')

        #last letters
        result_list.append(processAlpha(initial_list[3]))
        result_list.append(processAlpha(initial_list[4]))
        result_list.append(processAlpha(initial_list[5]))

    elif len(initial_list) == 8:
        if processAlpha(initial_list[0]) == 'B' and initial_list[1].isnumeric() == True:
            result_list.append('B')

            result_list.append(' ')
            
            #numbers
            result_list.append(processNumber(initial_list[1]))
            result_list.append(processNumber(initial_list[2]))
            result_list.append(processNumber(initial_list[3]))

            result_list.append(' ')

            #last letters
            result_list.append(processAlpha(initial_list[4]))
            result_list.append(processAlpha(initial_list[5]))
            result_list.append(processAlpha(initial_list[6]))

        else:
            #first letters
            result_list.append(processAlpha(initial_list[0]))
            result_list.append(processAlpha(initial_list[1]))

            result_list.append(' ')

            #numbers
            result_list.append(processNumber(initial_list[2]))
            result_list.append(processNumber(initial_list[3]))

            result_list.append(' ')

            #last letters
            result_list.append(processAlpha(initial_list[4]))
            result_list.append(processAlpha(initial_list[5]))
            result_list.append(processAlpha(initial_list[6]))

    else:
        print("Error : plate not correct")
        result_list = initial_list

    result_text = ""
    if None in result_list:
        print("Error : plate detected None")
    else:
        result_text = result_text.join(result_list)

    return result_text

#extracts text form licence plate image
def extract_plate_text(img):
    
    img = cv2.resize(img, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5,5), 0)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    rectangle = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    img = cv2.dilate(img, rectangle, iterations = 1)

    text = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
    
    if len(text) < 6:
        print("\n\nERROR plate : ", text, "\n\n")
    else:
        text = process_plate_text(text)
        print("\n\nPlate Detected : ", text, "\n\n")

def ocr_image(path):
    img = cv2.imread(path)
    
    extract_plate_text(img)
    cv2.imwrite(path, img)
