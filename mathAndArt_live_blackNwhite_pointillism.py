import cv2

def skip(n):
    pass

#cam config
cam = cv2.VideoCapture(int(input('Enter 0 for default webcam\n')))
width, height = 640, 480
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

pointillism = cv2.resize(cv2.imread('mathAndArt/blank.jpg'), dsize=(width, height), interpolation=cv2.INTER_AREA)

cv2.namedWindow('Original')
cv2.createTrackbar('r Size %', 'Original', 0, 100, skip)
cv2.setTrackbarPos('r Size %', 'Original', 100)
cv2.createTrackbar('tile Size', 'Original', 1, 10, skip)
cv2.setTrackbarPos('tile Size', 'Original', 4)
cv2.createTrackbar('light CALB', 'Original', 0, 50, skip)
cv2.setTrackbarPos('light CALB', 'Original', 10)

while True:
    #camread
    ret, original = cam.read()

    #init
    tileSize = cv2.getTrackbarPos('tile Size', 'Original')
    B, G, R = 0, 0, 0
    cv2.rectangle(pointillism, (0,0), (width, height), (255, 255, 255), cv2.FILLED)

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
            cv2.circle(pointillism, (tileX*tileSize + int(tileSize/2), tileY*tileSize + int(tileSize/2)), r, (0, 0, 0), cv2.FILLED)
            B, G, R = 0, 0, 0
    
    #Display img
    cv2.imshow('Original', original)
    cv2.imshow('Pointillism', pointillism)

    #exit
    if cv2.waitKey(1) > 0: break

#cache release & close window
cam.release()
cv2.destroyAllWindows()
