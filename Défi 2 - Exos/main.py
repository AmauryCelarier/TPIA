import cv2
import sys

img = cv2.imread("JordanCoubeh.png")

if img is None:
    sys.exit("Impossible de lire l'image")

cv2.imshow("Image", img)
cv2.waitKey(0)