import cv2
import numpy as np

#emphasized version

#cam config
cam = cv2.VideoCapture(int(input('Enter 0 for default webcam\n')))
width, height = 640, 480
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def nothing(pos):
    pass

cv2.setUseOptimized(True)
cv2.namedWindow('Pointillism Vison')
cv2.createTrackbar('Emphasize', 'Pointillism Vison', 1, 10, nothing)
cv2.setTrackbarPos('Emphasize', 'Pointillism Vison', 8)

tileSize = 4

def emphasize(colVal):
    emphasize = 0.1 * cv2.getTrackbarPos('Emphasize', 'Pointillism Vision')

    deviation = abs(255/2-colVal)
    if colVal > 255/2:
        return colVal + deviation ** emphasize
    else:
        return colVal - deviation ** emphasize
    
while True:
    #camread
    ret, original = cam.read()
    cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    pointillism = np.zeros((height, width, 3), np.uint8)
    cv2.rectangle(pointillism, (0,0), (width, height), (255,255,255), cv2.FILLED)
    L = 0

    #BGR Extraction & drawing shapes
    for tileX in range(int(width/tileSize)):
        for tileY in range(int(height/tileSize)):
            for pixelX in range(tileSize):
                for pixelY in range(tileSize):
                    pos = tileY*tileSize+pixelY, tileX*tileSize+pixelX
                    L += emphasize(int(original[pos][0]))
            L /= tileSize ** 2
            brightness = 1 - L / 255

            r = int(tileSize * brightness)
            circleMid = (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2))
            cv2.circle(pointillism, circleMid, r, (0, 0, 0), cv2.FILLED)
            L = 0
    
    #Display img
    cv2.imshow('Pointillism Vison', cv2.hconcat([original, pointillism]))

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cam.release()
cv2.destroyAllWindows()