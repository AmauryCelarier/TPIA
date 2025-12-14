import cv2 as cv
import numpy as np
imgNG = np.zeros((256,512,1), np.float32)

for i in range(imgNG.shape[0]):
    for j in range(imgNG.shape[1]):
        imgNG[i, j] = (np.cos((i + j) / 512.0 * 6.28 * 10.0) + 1.0) / 2.0

cv.imshow("Image en niveaux de gris", imgNG)
imgCoul = np.zeros((256, 512, 3), np.uint8)
for i in range(imgCoul.shape[0]):
    for j in range(imgCoul.shape[1]):
        # Composante Bleu :
        imgCoul[i, j, 0] = int((np.cos((i + j) / 512.0 * 6.28 * 10.0) + 1.0) * 127)
        # Composante Vert :
        imgCoul[i, j, 1] = int((np.cos((i + j) / 512.0 * 6.28 * 5.0) + 1.0) * 127)
        # Composante Rouge :
        imgCoul[i, j, 2] = int((np.cos((i + j) / 512.0 * 6.28 * 2.5) + 1.0) * 127)

cv.imshow("Image en couleur", imgCoul)
cv.waitKey(0)
cv.destroyAllWindows()  