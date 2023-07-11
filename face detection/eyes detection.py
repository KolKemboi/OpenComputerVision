import cv2

image = cv2.imread("img.jpg", cv2.IMREAD_UNCHANGED)
gray_face = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


faces = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5)

to_detect = list()
eyes_detected = list()

for (x, y, w, h) in faces:
	face = image[y: y+h, x: x+w]
	to_detect.append(face)

for face in to_detect:
	eyes = eye_cascade.detectMultiScale(face, scaleFactor = 1.3, minNeighbors = 20)
	for (x, y, w, h) in eyes:
		cv2.rectangle(to_detect[0], (x, y), (x + w, y + h), (0, 0, 255), 3 )



cv2.imshow("face", to_detect[0])
"""
cv2.imshow("gray_image", gray_face)

for indx, face in enumerate(to_detect):
	cv2.imshow(f"face_{indx}", face)
"""
cv2.waitKey(0)
cv2.destroyAllWindows()