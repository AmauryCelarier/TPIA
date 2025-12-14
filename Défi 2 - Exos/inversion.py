import cv2
import numpy
import sys
import os

output_path = "image_couleur_negative.png"

img_originale = cv2.imread("JordanCoubeh.png")

if img_originale is None:
    sys.exit(f"Erreur: Impossible de lire l'image à partir de JordanCoubeh.png")

img_negative = 255 - img_originale

cv2.imshow("Image Originale", img_originale)
cv2.imshow("Image Négative", img_negative)

success = cv2.imwrite(output_path, img_negative)

if success:
    print(f"L'image négative a été sauvegardée avec succès sous : {os.path.abspath(output_path)}")
else:
    print("Erreur lors de la sauvegarde de l'image.")

cv2.waitKey(0)
cv2.destroyAllWindows()