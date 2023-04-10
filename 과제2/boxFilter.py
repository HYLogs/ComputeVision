import cv2

img = cv2.imread("img/book.png")

if img is not None:
    filterd_img = cv2.boxFilter(img, -1, (5, 5), normalize=True)
    cv2.imshow('IMG', filterd_img)
    cv2.waitKey()