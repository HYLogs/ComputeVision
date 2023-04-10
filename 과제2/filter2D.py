import cv2
import numpy as np

img = cv2.imread("img/book.png")

if img is not None:
    kernel = np.ones((3, 3), dtype=np.float64)
    kernel[1, :] = 0
    kernel[2, :] = -1
    print(kernel)

    filterd_img = cv2.filter2D(img, -1, kernel) # -1은 원본 데이터 타입을 사용
    cv2.imshow('IMG', filterd_img)
    cv2.waitKey()