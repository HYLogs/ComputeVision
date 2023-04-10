import cv2
import numpy as np

img = cv2.imread("img/book.png")

if img is not None:
    kernel = np.array([[-1, -2, -3, -2, -1],
                       [-2, -4, -6, -4, -2],
                       [0, 0, 0, 0, 0],
                       [2, 4, 6, 4, 2],
                       [1, 2, 3, 2, 1]]) # solbel
    print(kernel)

    filterd_img = cv2.filter2D(img, -1, kernel) # -1은 원본 데이터 타입을 사용
    cv2.imshow('IMG', filterd_img)
    cv2.waitKey()