import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([0,0,0])
	upper_blue = np.array([255, 255, 255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	x_cood, y_cood = frame.shape[1], frame.shape[0]

	result = cv2.bitwise_or(frame, frame, mask = mask)

	
	cv2.imshow("Vid Feed", result)

	if cv2.waitKey(1) == ord("q"):
		print(x_cood, y_cood)
		print(frame.shape)
		break

cap.release()
cv2.destroyAllWindows()
