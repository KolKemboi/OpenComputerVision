import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	b_w = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	x_cood, y_cood = frame.shape[1], frame.shape[0]
	corners = cv2.goodFeaturesToTrack(b_w, 100, 0.1, 10)

	corners = np.int0(corners)

	for corner in corners:
		corner = tuple(np.ravel(corner))
		cv2.circle(frame, corner, 3, (0, 0, 255), 1) 

	cv2.imshow("frame", frame)

	if cv2.waitKey(1) == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()