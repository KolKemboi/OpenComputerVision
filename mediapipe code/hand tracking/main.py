import cv2
import mediapipe as mp

image = cv2.imread("hand.jpg", cv2.IMREAD_COLOR)
gray_hand = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#model initialization
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
		min_detection_confidence = 0.5,
		min_tracking_confidence = 0.5
	)

mp_drawing = mp.solutions.drawing_utils

image.flags.writeable = False
results = holistic_model.process(image)
image.flags.writeable = True



mp_drawing.draw_landmarks(
		image,
		results.left_hand_landmarks,
		mp_holistic.HAND_CONNECTIONS

	)


cv2.imshow("hand", image)
cv2.imshow("gray_hand", gray_hand)

cv2.waitKey(0)
cv2.destroyAllWindows()