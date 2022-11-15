'''Testing YOGA DayOne'''

import cv2

cap = cv2.VideoCapture(0) #cam select

while cap.isOpened():    #keep showing frame if cam is open until q pressed 
    ret, frame = cap.read()
    cv2.imshow('ElectroStream', frame) #set frame name 
    
    if cv2.waitKey(10) :  # terminate with cv2.waitKey(10) & 0xFF == ord('key')
        continue
        
cap.release()
cv2.destroyAllWindows()
