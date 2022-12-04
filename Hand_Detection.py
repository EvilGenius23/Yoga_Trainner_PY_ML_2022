#Import nessoery libraries 
import cv2
import mediapipe as mp

#create variabe to store body skeleton
sk = mp.solutions.holistic


#create a variable to store human hand
human_hand=sk.Holistic(min_detection_confidence=0.2 , min_tracking_confidence=0.2)


#create drawing element which hwp us to draw over screen 
my_drawing=mp.solutions.drawing_utils #create a obj to draw over screen



#create camera to get pixles from cam 
cap = cv2.VideoCapture(0) #cam select as defalt to system 




#create a loop to do all activities 
while cap.isOpened():    #keep showing frame if cam is open until q pressed 
    ret, frame = cap.read()
    

    hand=human_hand.process(frame);



    #draw right hand 
    my_drawing.draw_landmarks(frame,hand.right_hand_landmarks,sk.HAND_CONNECTIONS)
    
    #draw lef land
    my_drawing.draw_landmarks(frame,hand.left_hand_landmarks,sk.HAND_CONNECTIONS)
    
    
    cv2.imshow('Title', frame)

    cv2.waitKey(2)


cap.release()
cv2.destroyAllWindows()
