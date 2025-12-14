import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erreur: pas accès à la webcam.")
else:
    print("Accès à la webcam !")

ret = True
while ret:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == 27:
            ret = False
    else:
        print("Erreur lors de la capture de l'image.")
cv2.destroyAllWindows()
cap.release()
    
