import cv2
import numpy as np
import time
import os
import imutils
from ultralytics import YOLO

def object_detection_test(im, conf=0.28, return_count=False):
    cv2.imwrite('./captured/' + 'photo.jpg', im)
    model = YOLO('yolov8x.pt')
    results = model.predict('./captured/' + 'photo.jpg', conf=conf)
    n_objects = results[0].__len__()
    if return_count:
        return n_objects
    if n_objects > 1:
        print('sus')
        return False
    print('empty')
    return True

def capture_photo(dataset_path='./captured/', filename='photo.jpg'):
    # Open the camera (0 is the default camera index)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a single frame from the camera
    ret, frame = cap.read()

    if ret:
        # Save the captured frame as an image file
        cv2.imwrite(dataset_path + filename, frame)
        print(f"Photo saved as {filename}")
    else:
        print("Error: Could not capture frame.")

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
    return frame

def diff_test(im_empty, im_test):
    diff = np.minimum(im_empty - im_test, im_test - im_empty)
    indices = np.where((50 > diff))
    for idx in zip(indices[0], indices[1], indices[2]):
        diff[idx] = 0

    if np.sum(diff) == 0:
        print('empty')
        return True
    else:
        print('sus')
        return False

def image_registration_test(im_empty, im_test):
    
    img1 = cv2.cvtColor(im_empty, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(im_test, cv2.COLOR_BGR2GRAY)

    orb_detector = cv2.ORB_create(5000)
    kp1, d1 = orb_detector.detectAndCompute(img1, None)
    kp2, d2 = orb_detector.detectAndCompute(img2, None)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(d1, d2)

    # Sort matches by their distance (lowest distance is better)
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract the matched keypoints' coordinates
    p1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    p2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

    if np.sum(mask) / len(mask) > 0.96 and np.sum(np.abs(homography - np.identity(3))) < 0.3:
        print('empty')
        return True
    else:
        print('sus')
        return False

def detect(im_empty, im_test):
    # test diff
    diff_result = diff_test(im_empty, im_test)

    # test registration
    image_registration_result = image_registration_test(im_empty, im_test)

    # object detection test
    object_detection_result = object_detection_test(im_empty, im_test)

    return [diff_result, image_registration_result, object_detection_result]
    
def main():
    # setup
    dataset_path = './captured/'
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
    t = time.time()
    print(t)
    im_empty = cv2.imread('photo_0.jpg')

    # open camera for 5 secs to adjust to light
    cap = cv2.VideoCapture(0)
    while time.time() < t + 5:
        ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    # capture the photo
    im_test = capture_photo(dataset_path, f'photo_{t}.jpg')

    result = detect(im_empty, im_test)
    print(result)

    


if __name__ == "__main__":
    main()