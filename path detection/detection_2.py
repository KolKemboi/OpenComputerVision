import cv2
import numpy as np
import os

image = cv2.imread("road_img_1.jpg", cv2.IMREAD_COLOR)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaus_blur = cv2.GaussianBlur(gray_img, (5, 5), 0)
edges = cv2.Canny(image, 400, 400)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20, 100, 100], dtype = np.uint8)
upper_yellow = np.array([30, 255, 255], dtype = np.uint8)

mask_yellow = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
mask_white = cv2.inRange(gray_img, 200, 255)
mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
mask_yw_image = cv2.bitwise_and(gray_img, mask_yw)

"""

def region_of_interest(image, vertices):
	mask = np.zeros_like(img)

	mask_color = 255

	cv2.fillPoly(mask, vertices, mask_color)
	masked_

region_of_interest_vertices = [
	(200, height), (width/2, height/2), (width, heigth)
]

cropped_image = region_of_interest
"""
def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

lines = cv2.HoughLinesP(mask_yw_image, rho = 2, theta = np.pi/180,
	threshold = 50, lines = np.array([]), minLineLength = 10, maxLineGap = 30)

drawn = draw_lines(image, lines)
cv2.imshow("detection", drawn)


if os.path.isdir("lane_detection_images"):
	cv2.imwrite("lane_detection_images/gray_img.jpg", gray_img)
	cv2.imwrite("lane_detection_images/gaus_blur.jpg", gaus_blur)
	cv2.imwrite("lane_detection_images/image_edges.jpg", edges)
	cv2.imwrite("lane_detection_images/mask_yw_image.jpg", mask_yw_image)
	cv2.imwrite("lane_detection_images/detected.jpg", drawn)
else:
	os.mkdir("lane_detection_images")

cv2.waitKey(0)
cv2.destroyAllWindows()