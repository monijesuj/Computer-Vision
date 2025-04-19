import cv2

im_grey = cv2.imread('test.jpg', 0)

cv2.imshow('Test image', im_grey)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('grey_image.jpg', im_grey)