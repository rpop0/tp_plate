from classes.Recognizer import Recognizer

def main():
    print("Works")
    rec = Recognizer("media/golf.jpg")
    img, loc = rec.process_image()
    rec.process_number(img, loc)


if __name__ == "__main__":
    main()