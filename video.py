import cv2

def main():
    # Create a VideoCapture object to capture video from the default camera (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Main loop to continuously capture and display video frames
    while True:
        # Capture a frame
        ret, frame = cap.read()

        # If the frame was successfully captured, display it
        if ret:
            cv2.imshow('Video', frame)

            # Break the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not read a frame.")
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()