import cv2

image = cv2.imread("img.jpg", cv2.IMREAD_UNCHANGED)
gray_face = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5)

to_detect = list()
for (x, y, w, h) in faces:
	face = image[y: y+h, x: x+w]
	to_detect.append(face)

cv2.imshow("face", image)
cv2.imshow("gray_image", gray_face)

for indx, face in enumerate(to_detect):
	cv2.imshow(f"face_{indx}", face)

cv2.waitKey(0)
cv2.destroyAllWindows()