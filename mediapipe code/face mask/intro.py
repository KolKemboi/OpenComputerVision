import mediapipe as mp
import cv2

face = cv2.imread("img.jpg")
gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
	cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = face_cascade.detectMultiScale(
	gray_face,
	scaleFactor = 1.1,
	minNeighbors = 5
)

to_put_mask = list()

for (x, y, w, h) in faces:
	face = face[y: y+h, x: x+w]
	to_put_mask.append(face)

	

def faceMesh(input_face):
	mp_holistic = mp.solutions.holistic

	holistic_model = mp_holistic.Holistic(
			min_detection_confidence = 0.5,
			min_tracking_confidence = 0.5
		)

	mp_drawing = mp.solutions.drawing_utils

	rgb_face = cv2.cvtColor(input_face, cv2.COLOR_BGR2RGB)

	rgb_face.flags.writeable = False
	results = holistic_model.process(rgb_face)
	rgb_face.flags.writeable = True

	mp_drawing.draw_landmarks(\
		rgb_face,
		results.face_landmarks,
		mp_holistic.FACEMESH_CONTOURS,
		mp_drawing.DrawingSpec(
			color = (255, 0, 255),
			thickness = 1,
			circle_radius = 1
		),
		mp_drawing.DrawingSpec(
			color = (0, 255, 255),
			thickness = 1,
			circle_radius = 1
		)
	)
	return rgb_face

for face in to_put_mask:
	output = faceMesh(face)

cv2.imshow("face", output)


cv2.imwrite("output.jpg", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
