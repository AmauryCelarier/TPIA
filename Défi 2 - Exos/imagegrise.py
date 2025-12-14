import cv2 as cv
import numpy as np
# Création d'une image de taille 512x256 (256 lignes et 512 colonnes)
# en niveau de gris (1 canal) codée à l'aide d'unsigned short (np.uint16)
# Les valeurs des pixels sont comprises entre 0 (noir) et 65535 (blanc)
imgNG = np.zeros((256,512,1), np.uint16)
imgNG.fill(65535)
cv.imshow("Image en niveaux de gris", imgNG)
cv.waitKey(0)
cv.destroyAllWindows()
