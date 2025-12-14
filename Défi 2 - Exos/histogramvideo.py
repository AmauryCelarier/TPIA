import cv2 as cv
import numpy as np


def compute_histogram_ng(img, nb_classes):
    assert len(img.shape) == 3 
    hauteur, largeur = 512, 1024
    max_intensity = 256.0

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] # Bleu, Vert, Rouge
    channels = [0, 1, 2] # Canaux B, G, R

    histograms = []

    for c in channels:
        hist = cv.calcHist(images=[img], channels=[c], mask=None,
                           histSize=[nb_classes], ranges=[0.0, max_intensity])
        
        hist = cv.normalize(hist, hist, alpha=0, beta=1, norm_type=cv.NORM_MINMAX).flatten()
        histograms.append(hist)
    
    max_val = np.max([h.max() for h in histograms])

    img_hist_superposed = np.zeros((hauteur, largeur, 3), dtype=np.uint8)

    for c, hist in enumerate(histograms):
        color = colors[c]
        
        points = np.zeros((nb_classes, 1, 2), dtype=np.int32)
        
        for h_val in range(nb_classes):
            x = int((h_val * largeur / nb_classes) + (largeur / nb_classes / 2))
            
            y = int(hauteur - (hist[h_val] * hauteur)) 
            
            points[h_val] = (x, y)
                
        
        cv.polylines(img_hist_superposed, [points], False, color, 1)
                
    cv.imshow("Histogramme Couleur Superposé", img_hist_superposed)


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: pas accès à la webcam.")
else:
    print("Accès à la webcam ! Histogramme en temps réel démarré.")
    
    ret = True
    while ret:
        ret, frame = cap.read()

        if ret:

            cv.imshow("Webcam", frame)
            
            compute_histogram_ng(frame, 256)
            
            if cv.waitKey(1) == 27: 
                ret = False
        else:
            print("Erreur lors de la capture de l'image.")
            ret = False

    cv.destroyAllWindows()
    cap.release()
    print("Flux vidéo arrêté.")