import cv2
import time

def take_photo(file_name):
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Couldn't open camera")
        return
    time.sleep(2)

    ret, frame = camera.read()
    if ret:
        # Save the captured photo
        cv2.imwrite(file_name, frame)
        print("Photo captured and saved as", file_name)
    else:
        print("Error: Couldn't capture photo")

    camera.release()

def calculate_image_difference(image1, image2):

    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    if img1 is None:
        print("Error: Couldn't load", image1)
        return
    elif img2 is None:
        print("Error: Couldn't load", image2)
        return

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    mse = ((gray1 - gray2) ** 2).mean()

    return mse

def compare_images(image1, image2, threshold=100):
    mse = calculate_image_difference(image1, image2)
    if mse < threshold:
        print("Images are similar")
    else:
        print("Images are different")

if __name__ == "__main__":
 
    first_photo = "first_photo.jpg"
    take_photo(first_photo)

    
    print("Press Enter to take the second photo...")
    input()

    second_photo = "second_photo.jpg"
    take_photo(second_photo)

    compare_images(first_photo, second_photo)
