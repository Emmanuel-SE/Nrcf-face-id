def findEncodings (image):
    encodeList=[]
    for img in image:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encoded_face=face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face) 
    return encodeList      

encoded_face_train=findEncodings(image)