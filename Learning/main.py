import cv2

path = "assets/img1.jpg"

img = cv2.imread(path, 1)
##-1, cv2.IMREAD_COLOR (loads in with color)
##0, cv2.IMREAD_GRAYSCALE (loads in as gray scale)
##1, cv2.IMREAD_UNCHANGED (Loads in image with its alpha value)

img2 = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
img3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("new_img.jpg", img)

cv2.imshow("window", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()