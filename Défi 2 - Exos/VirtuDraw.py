import cv2 as cv
import numpy as np
import collections

blue_lower = np.array([105, 120, 100])
blue_upper = np.array([125, 255, 255])   

draw_color = (255, 0, 0)

draw_canvas = None

points = collections.deque(maxlen=512)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Erreur: pas accès à la webcam.")

else:
    print("Accès à la webcam !")

ret = True
while ret:
    ret, frame = cap.read()
    if ret:
        
        if draw_canvas is None:
            draw_canvas = np.zeros_like(frame, dtype=np.uint8)

        frame = cv.flip(frame, 1)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        mask = cv.inRange(hsv, blue_lower, blue_upper)

        mask = cv.erode(mask, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)

        contours, _ = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        center = None
        
        if len(contours) > 0:
            c = max(contours, key=cv.contourArea)
            
            ((x, y), radius) = cv.minEnclosingCircle(c)
            M = cv.moments(c)
            
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 5 :
                cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv.circle(frame, center, 5, (0, 0, 255), -1)

        points.appendleft(center)

        for i in range(1, len(points)):
            if points[i - 1] is None or points[i] is None:
                continue
            
            cv.line(draw_canvas, points[i - 1], points[i], draw_color, 5)

        frame = cv.addWeighted(frame, 1.0, draw_canvas, 0.9, 0)
        
        cv.imshow("Dessin Virtuel", frame)

        if cv.waitKey(1) == 27: 
            break
    else:
        print("Erreur lors de la capture de l'image.")
        break


cv.destroyAllWindows()
cap.release()