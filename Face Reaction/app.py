import cv2
import numpy as np
from fer import FER

scr = cv2.VideoCapture(0) #30fps
scr.set(3, 640)
scr.set(4, 480)

#init FRE (Facial expression recognition from images)
detector = FER(mtcnn=True)

while True:

    ret,frame = scr.read()
    # frame = cv2.flip(frame,1)

    #return emotion name and % of true detection
    emotion, score = detector.top_emotion(frame)

    print(emotion,score)
    if emotion == 'angry':
        emoj = cv2.imread('Reactions/angry.png')
    elif emotion == 'disgust':
        emoj = cv2.imread('Reactions/disgust.png')
    elif emotion == 'fear':
        emoj = cv2.imread('Reactions/fear.png')
    elif emotion == 'happy':
        emoj = cv2.imread('Reactions/happy.png')
    elif emotion == 'sad':
        emoj = cv2.imread('Reactions/sad.png')
    elif emotion == 'surprise':
        emoj = cv2.imread('Reactions/surprise.png')
    elif emotion == 'neutral':
        emoj = cv2.imread('Reactions/neutral.png')
    else:
        emoj = cv2.imread('Reactions/none.png')


    #Adding Image on Screen
    
    # Read emoj and resize
    size = 150
    emoj = cv2.resize(emoj, (size, size))

    # Create a mask of emoj
    img2gray = cv2.cvtColor(emoj, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

    roi = frame[-size-20:-20, -size-20:-20]
    # roi = frame[-size-310:-310, -size-470:-470]
    # Set an index of where the mask is
    roi[np.where(mask)] = 0
    roi += emoj


    #add text
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (40, 210)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    cv2.putText(frame,emotion, org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    #show screen
    cv2.imshow('frame',frame)
    
    #stop
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

scr.release()

cv2.destroyAllWindows()