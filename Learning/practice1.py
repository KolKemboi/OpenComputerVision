import cv2
import random
import numpy as np

img = np.ones((300,300,3))

for x in range(300):
	for y in range(300):
		img[x, y] = [random.randint(0,1),random.randint(0, 1),random.randint(0, 1)]

cv2.imshow("image_window", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
