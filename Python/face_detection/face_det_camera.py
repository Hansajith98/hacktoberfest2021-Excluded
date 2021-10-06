import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
                  
    #g_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    #conv img into greyscale
    face = face_cascade.detectMultiScale(frame,      #search for eye in img
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    eye = eye_cascade.detectMultiScale(frame,      #search for eye in img
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)  #drawing_rectangle
    for x,y,w,h in eye:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)  #drawing_rectangle
       
    cv2.imshow('frame',frame)   #imshow --displaying frame
    #cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

