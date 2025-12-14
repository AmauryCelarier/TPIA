import cvzone
from cvzone.ColorModule import ColorFinder
import cv2
import socket

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

success, img = cap.read() 
h,w,_ = img.shape

myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 96, 'smin': 145, 'vmin': 37, 'hmax': 119, 'smax': 254, 'vmax': 246}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
      
    success, img = cap.read()
    imgColor, mask = myColorFinder.update(img,hsvVals)
    imgContour, contours = cvzone.findContours(img,mask)

    if contours:
        data = contours[0]['center'][0],\
        h-contours[0]['center'][1],\
        int(contours[0]['area'])
        print(data)
        sock.sendto(str.encode(str(data)), serverAddressPort)


    # imgStack = cvzone.stackImages([img, imgColor, mask, imgContour],2,0.5)
    # cv2.imshow ("Image", imgStack)
    imgContour = cv2.resize(imgContour,(0,0),None,0.3,0.3 )
    cv2.imshow ("Image Contour", imgContour)
    cv2.waitKey(1)
    