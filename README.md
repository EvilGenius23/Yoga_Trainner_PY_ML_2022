# Yoga_Trainner_PY_ML_2022

Computer Vission / ML Based Yoga Trainner (Assistant) 


'''Testing YOGA DayOne'''

////Installing Required Libraries//// 


![alt text](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)


Python 3.10:

https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe


------------------------------------------------------------------


![alt text](https://editor.analyticsvidhya.com/uploads/53474logo_horizontal_color.png)


MediaPipe: 

```$ python3 -m venv mp_env && source mp_env/bin/activate```

Install MediaPipe Python package and start Python interpreter:

```(mp_env)$ pip install mediapipe```

```(mp_env)$ python3```

testing installation:

In Python interpreter, import the package and start using one of the solutions:

```import mediapipe as mp```

```mp_face_mesh = mp.solutions.face_mesh```



------------------------------------------------------------------


![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/800px-OpenCV_Logo_with_text_svg_version.svg.png)

OpenCV :

OpenCV can be directly downloaded and installed with the use of pip (package manager).
To install OpenCV, just go to the command-line and type the following command:

```$pip install opencv-python```



------------------------------------------------------------------

```
import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()
    cv2.imshow('ElectroStream', frame)     
    if cv2.waitKey(10) :  # terminate with cv2.waitKey(10) & 0xFF == ord('key')
        continue
        
        
cap.release()

cv2.destroyAllWindows()

```

#end Day1 ;)  </>
