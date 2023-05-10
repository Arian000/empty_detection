import cv2
import numpy as np

def capture_photo(filename='photo.jpg'):
    # Open the camera (0 is the default camera index)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a single frame from the camera
    ret, frame = cap.read()

    if ret:
        # Save the captured frame as an image file
        cv2.imwrite(filename, frame)
        print(f"Photo saved as {filename}")
    else:
        print("Error: Could not capture frame.")

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()
    return frame

if __name__ == "__main__":
    frame = capture_photo('photo.jpg')
    # np.save('photo', frame)
    # filename = 'photo.npy'
    # old_frame = np.load(filename)
    # print(old_frame.shape)
    # diff = np.minimum(old_frame-frame, frame-old_frame)
    # print(diff)

    
    # indices = np.where((50 > diff))
    # for idx in zip(indices[0], indices[1], indices[2]):
    #     # print(idx)
    #     diff[idx] = 0
    # print(diff)

    # cv2.imwrite('diff.jpg', diff)