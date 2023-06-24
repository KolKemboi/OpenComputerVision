import cv2 
import numpy as np
import os

image_path = os.path.join("assets","image_1.png")
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

edges = cv2.Canny(image, 50, 150)
cv2.imshow("image", edges)
out_image = os.path.join("outputs","output_1.png")
cv2.imwrite(out_image, edges)
cv2.waitKey(0)
cv2.destroyAllWindows()