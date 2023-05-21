import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	x, y = frame.shape[0], frame.shape[1]



	frame = cv2.resize(frame, (200, 200))
	new_x, new_y = frame.shape[0], frame.shape[1]
	#print(*(new_x, new_y), sep=' ', end='\n', file=sys.stdout)

	new_image = cv2.resize(frame, (new_x*2, new_y*2))

	#new_image = np.eye((new_x*4, new_y*4))
	
	frame_2 = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
	frame_3 = cv2.rotate(frame, cv2.ROTATE_180)
	frame_4 = cv2.rotate(frame, cv2.ROTATE_180)
	new_image[0: new_x, 0: new_y] = frame
	new_image[new_x: new_x *2 ,new_y : new_y*2] = frame
	new_image[0 : new_x , new_y: new_y*2] = frame
	new_image[new_x: new_x *2, 0: new_y] = frame

	cv2.imshow("vid", new_image)

	if cv2.waitKey(1) == ord("q"):
		print(*(x, y), sep=' ', end='\n', file=sys.stdout)

		print(*(new_x, new_y), sep=' ', end='\n', file=sys.stdout)
		break

cap.release()
cv2.destroyAllWindows()