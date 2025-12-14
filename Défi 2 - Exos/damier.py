import cv2 as cv
import numpy as np


hauteur = 256  
largeur = 512  
nb_canaux = 1
type_donnees = np.uint16 
valeur_max = 65535      

img_damier = np.zeros((hauteur, largeur, nb_canaux), dtype=type_donnees)

i, j = np.indices((hauteur, largeur))   

img_damier[:, :, 0] = ((i + j) % 2 == 0).astype(type_donnees) * valeur_max

cv.imshow("Image Damier (16 bits)", img_damier)
cv.waitKey(0)
cv.destroyAllWindows()