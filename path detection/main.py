import cv2
import os
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread("road_img_3.jpg", cv2.IMREAD_UNCHANGED)

gray_road = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaus_blur = cv2.GaussianBlur(gray_road, (5, 5), 0)

edges = cv2.Canny(gaus_blur, 50, 150)

mask = np.zeros_like(edges)

height, width = image.shape[:2]
roi_vertices = [(0, height), (width / 2, height / 2), (width, height)]
mask_color = 255
cv2.fillPoly(mask, np.array([roi_vertices], dtype = np.int32), mask_color)
masked_edges = cv2.bitwise_and(edges, mask)

lines = cv2.HoughLinesP(masked_edges, rho = 6, theta = np.pi/60, threshold = 160, minLineLength = 40, maxLineGap = 25)

line_image = np.zeros_like(image)

for ind, line in enumerate(lines):
	x1, y1, x2, y2 = line[0]
	cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)

final_image = cv2.addWeighted(image, 0.8, line_image, 1, 0)

cv2.imshow("image", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()