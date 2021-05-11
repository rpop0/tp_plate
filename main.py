from classes.Recognizer2 import Recognizer2

def main():
    rec = Recognizer2("media/1.jpg")

    #usess functions from rec to get necesary input
    img_edges, img_gray = rec.process_image()
    contours = rec.process_contours(img_edges)
    loc = rec.select_plate(contours)
    img_cut = rec.mask_plate(loc, img_gray)

    #runs plate verification
    rec.process_number(img_cut, loc)


if __name__ == "__main__":
    main()

'''

TO DO

NEED
- better contour detection
- adjust the text recodnition
- add suport for video (brake to frames ???)

NICE TO HAVE
- overlays on video playback
- ability to conect to server/ip camera ???
- brake number plates to characters before recognition

'''