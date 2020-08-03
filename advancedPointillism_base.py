import cv2
import numpy as np

def skip(n):
    pass

#cam config
cam = cv2.VideoCapture(int(input('Enter 0 for default webcam\n')))
width, height = 640, 480
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

tileSizes = []
for n in range(1, height, 1):
    if height % n == 0 and width % n == 0:
        tileSizes.append(n)

cv2.namedWindow('Original')
cv2.createTrackbar('#Tile', 'Original', 2, len(tileSizes), skip)
#4 or 8 on 640*480
cv2.setTrackbarPos('#Tile', 'Original', 8)
cv2.createTrackbar('r Size %', 'Original', 0, 100, skip)
cv2.setTrackbarPos('r Size %', 'Original', 100)
cv2.createTrackbar('light CALB', 'Original', 0, 50, skip)
cv2.setTrackbarPos('light CALB', 'Original', 10)
cv2.createTrackbar('BW_COL', 'Original', 0, 1, skip)
cv2.setTrackbarPos('BW_COL', 'Original', 1)

while True:
    #camread
    ret, original = cam.read()
    
    #init
    tileSize = cv2.getTrackbarPos('#Tile', 'Original')
    B, G, R = 0, 0, 0
    pointillism_CL = np.zeros((height, width, 3), np.uint8)
    pointillism_BW = pointillism_CL.copy()

    if cv2.getTrackbarPos('BW_COL', 'Original') == 0:
        BW_COL = (0, 0, 0)
        BW_DOT_COL = (255, 255, 255)
    else:
        BW_COL = (255, 255, 255)
        BW_DOT_COL = (0, 0, 0)
    cv2.rectangle(pointillism_BW, (0,0), (width, height), BW_COL, cv2.FILLED)

    #BGR Extraction & drawing shapes
    for tileX in range(int(width/tileSize)):
        for tileY in range(int(height/tileSize)):
            for pixelX in range(tileSize):
                for pixelY in range(tileSize):
                    pos = tileY*tileSize+pixelY, tileX*tileSize+pixelX
                    B += int(original[pos][0]) + cv2.getTrackbarPos('light CALB', 'Original')
                    G += int(original[pos][1]) + cv2.getTrackbarPos('light CALB', 'Original')
                    R += int(original[pos][2]) + cv2.getTrackbarPos('light CALB', 'Original')
            B /= tileSize ** 2
            G /= tileSize ** 2
            R /= tileSize ** 2
            brightness = 1 - (B+G+R) / (255*3)

            r = int(tileSize * brightness * 0.01 * cv2.getTrackbarPos('r Size %', 'Original'))
            cv2.circle(pointillism_CL, (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2)), r, (B, G, R), cv2.FILLED)
            cv2.circle(pointillism_BW, (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2)), r, BW_DOT_COL, cv2.FILLED)
            B, G, R = 0, 0, 0
    
    #Display img
    cv2.imshow('Original', original)
    cv2.imshow('Pointillism_BW', pointillism_BW)
    cv2.imshow('Pointillism_CL', pointillism_CL)

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cam.release()
cv2.destroyAllWindows()