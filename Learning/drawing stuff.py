import cv2
import numpy as np 
import sys


cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	#frame = cv2.resize(frame, (1366, 780))

	x_max, y_max = int(frame.shape[1]), int(frame.shape[0])

	font = cv2.FONT_HERSHEY_SIMPLEX


	img = cv2.line(frame, (0, 0), (x_max, y_max), (0, 0, 255), 10)
	img = cv2.line(img, (0, y_max), (x_max, 0), (0, 0, 0), 10)
	img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 4)
	img = cv2.circle(img, (300, 300), 120, (120, 255, 0), 4)
	img = cv2.putText(img, "Kol is fucking AMAZING", (200, 300), font, 1,  (255, 255, 255), 3, cv2.LINE_AA)

	cv2.imshow("window", img)

	if cv2.waitKey(1) == ord("q"):
		print(*(x_max, y_max), sep=' ', end='\n', file=sys.stdout)
		print(frame.shape, sep=' ', end='\n', file=sys.stdout)
		break

cap.release()
cv2.destroyAllWindows()