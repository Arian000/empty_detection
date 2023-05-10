import numpy as np
import imutils
import cv2
import os


khali = cv2.imread('photo_0.jpg')
directory = './data/'
for filename in os.listdir(directory):
    try:
        test = cv2.imread(directory + filename)
        
        img1 = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(khali, cv2.COLOR_BGR2GRAY)
        height, width = img2.shape

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
        print(filename, np.sum(mask) / len(mask), len(mask))
        print(np.sum(np.abs(homography - np.identity(3))))
        transformed_img = cv2.warpPerspective(test, homography, (width, height))
        matchedVis = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)
        matchedVis = imutils.resize(matchedVis, width=1000)
        # cv2.imshow('Matched Visualization', matchedVis)  # Add a window name
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()  # Close all windows when done

        if np.sum(mask) / len(mask) > 0.96 and np.sum(np.abs(homography - np.identity(3))) < 0.3:
            print('empty')
        else:
            print('sus')
    except:
        print('very sus')

