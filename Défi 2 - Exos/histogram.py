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

    print("\nAffichage séparé (Histogramme par canal) :")
    for c, hist in enumerate(histograms):
        img_hist_sep = np.zeros((hauteur, largeur), dtype=np.uint8)
        color = colors[c]
        
        for h_val in range(nb_classes):
            p1 = (int(h_val * largeur / nb_classes), hauteur)
            p2 = (int((h_val + 1) * largeur / nb_classes),
                  int(hauteur - (hist[h_val] / max_val) * hauteur))
            
            cv.rectangle(img_hist_sep, p1, p2, (255), -1)
            cv.rectangle(img_hist_sep, p1, p2, (127), 1)

        cv.imshow(f"Hist. Canal {c} ({'B' if c==0 else ('G' if c==1 else 'R')})", img_hist_sep)

    img_hist_superposed = np.zeros((hauteur, largeur, 3), dtype=np.uint8)

    print("Affichage superposé (Courbes de Contour) :")

    for c, hist in enumerate(histograms):
        color = colors[c]

        points = np.zeros((nb_classes, 1, 2), dtype=np.int32)
        
        for h_val in range(nb_classes):
            x = int((h_val * largeur / nb_classes) + (largeur / nb_classes / 2))
            
            y = int(hauteur - (hist[h_val] * hauteur)) 
            
            points[h_val] = (x, y)
                
        
        cv.polylines(img_hist_superposed, [points], False, color, 1)
                
    cv.imshow("Histogramme Couleur Superposé", img_hist_superposed)


img = cv.imread("JordanCoubeh.png")

compute_histogram_ng(img, 256)

cv.waitKey(0)
cv.destroyAllWindows()