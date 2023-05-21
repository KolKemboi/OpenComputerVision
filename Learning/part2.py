import cv2
import random

path = "assets/img2.jpg"

img = cv2.imread(path, -1)
img = cv2.resize(img, (0, 0), fx = 0.75, fy = 0.75)

for x in range(30):
	for j in range(img.shape[1]):
		img[x][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

part = img[60:100, 60:100]
img[20:60, 20:60] = part

cv2.imshow("window", img)

cv2.waitKey(0)
cv2.destroyAllWindows()