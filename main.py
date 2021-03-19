from classes.Recognizer import Recognizer

def main():
    print("Works")
    rec = Recognizer("media/logan.jpg")
    rec.process_image()


if __name__ == "__main__":
    main()