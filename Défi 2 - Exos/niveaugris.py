import cv2

img = cv2.imread("JordanCoubeh.png")
if img is None:
    sys.exit(f"Erreur: Impossible de lire l'image à partir de JordanCoubeh.png")

img_ng = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image niveau gris',img_ng)

# Question 4 : conversion en différents espaces de couleur

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('image RGB',img_rgb)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image HSV',img_hsv)

img_hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow('image HSL',img_hsl)

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow('image YUV',img_yuv)

img_ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('image YCbCr',img_ycbcr)

img_cie_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow('image CIE-Lab',img_cie_lab)

img_xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
cv2.imshow('image XYZ',img_xyz)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()