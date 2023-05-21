import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	y_cood, x_cood = frame.shape[0], frame.shape[1]

	font = cv2.FONT_HERSHEY_SIMPLEX

	frame = cv2.line(frame, (0, 0), (x_cood, y_cood), (0, 0, 255) , 4)
	frame = cv2.rectangle(frame, (0, 0), (200, 200), (0, 255, 0), 1)
	

	cv2.imshow("vid feed", frame)

	if cv2.waitKey(1) == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()