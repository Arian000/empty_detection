import cv2
import numpy as np
import os


khali = cv2.imread('photo_0.jpg')
directory = './data/'
for filename in os.listdir(directory):
    test = cv2.imread(directory + filename)
    
    diff = np.minimum(khali-test, test-khali)
    # cv2.imshow('Image Title', diff)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    

    indices = np.where((50 > diff))
    for idx in zip(indices[0], indices[1], indices[2]):
        # print(idx)
        diff[idx] = 0

    if np.sum(diff) != 0:
        print(filename, 'por')
    else:
        print(filename, 'khali')
    # cv2.imshow('Image Title', diff)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imwrite('diff.jpg', diff)