

import cv2

path = "img.jpg"

image = cv2.imread(path, 0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 3)
	frame = image[y:y + h, x:x + w]

print(x, y, x + w, y + h)

cv2.imshow("image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
vid = cv2.VideoCapture(0)

while True:
	ret, frame = vid.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

	for (x, y, w, h) in faces:
		cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 3)
		frame = gray[y:y + h, x:x + w]
	
	cv2.imshow("vid", frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

vid.release()
cv2.destroyAllWindows()
"""
