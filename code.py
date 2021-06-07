import cv2
import numpy as np
import face_recognition
import os
import datetime
import pyrebase
#from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyAGwaYIE3eTwWEkNp_QvmvHpcvUEAvGiIw",
    "storageURL": "gs://facegrab-c82ff.appspot.com/",
    "databaseURL": "https://facegrab-c82ff-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "authDomain": "facegrab-c82ff.firebaseapp.com",
    "projectId": "facegrab-c82ff",
    "storageBucket": "facegrab-c82ff.appspot.com",
    "messagingSenderId": "414897340300",
    "appId": "1:414897340300:web:39698616f4a6c951fca0a9",
    "measurementId": "G-0F42EJJR32"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage=firebase.storage()
path_on_db = "/ImageSourceDirectory"
path = 'ImageSourceDirectory'
noww = datetime.datetime.now()
datenow = noww.strftime('%Y-%m-%d')
timenow = noww.strftime('%H:%M:%S')

images = []
classRollnos = []
myList = os.listdir(path)
camname = { 0 :"Webcam", 1 : "Living Room" }
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classRollnos.append(os.path.splitext(cl)[0])
print(classRollnos)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#INSERT DATA db
#data={'Name':"PRIYANSH VERMA",'Location':"webcam",'Date':"06/05/21",'Time':"09:21:24"}
#db.child("csvTable").child("0206cs181118").set(data)
#data = {'Name': name , 'Location': camname.get(caplist.get(cap)) , 'Date': datenow, 'Time': timenow}
#db.child("csvTable").child(name).set(data)
#DOWNLOAD FILE storage
#cloudfilename=input("File name in storage: ")
#print(storage.child(cloudfilename).get_url(None))
#downloadlink=input("URL: ")
#storage.child(downloadlink).download(img)

#

def timelocated(name, cap):
    noww = datetime.datetime.now()
    datenow = noww.strftime('%Y-%m-%d')
    timenow = noww.strftime('%H:%M:%S')
    personname = db.child("idTable").order_by_key().equal_to(name).get()
    for person in personname.each():
        studentname = person.val()['Name']
    #data = {'Name': studentname, 'Location': camname.get(caplist.get(cap)), 'Date': datenow, 'Time': timenow}
    data = {'Name': studentname, 'Location': [camname.get(caplist.get(cap)),  datenow,  timenow]}
    db.child("csvTable").child(name).set(data)
    user = db.child("csvTable").get()
    users = user.val()
    val = False
    for i in users:
        if i == name :
            val = True
    if val == True:
        db.child("csvTable").child(name).update({"Location" :[ camname.get(caplist.get(cap)) , datenow , timenow] })
        #db.child("csvTable").child(name).update({"Date": datenow})
        #db.child("csvTable").child(name).update({"Time": timenow})

    else:
        val =False


encodeListKnown = findEncodings(images)
print("Encoding Complete")


# code for getting all the cameras starts here:
index = 0  # starting index for the cameras : 0 being the webcam
getcam = []  # empty list for the camera indexing
caplist = {}  # a dictionary which will store the stream and the index
while True:
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
    if not cap.read()[0]:
        break
    else:
        getcam.append(index)
    cap.release()
    index += 1
print(getcam)
# the above code is for getting the cameras which are currently working in the machine
# it checks the all the 0 to n ports for cameras and whichever port returns a camera
# it gets stored in #getcam list Example = [0,1] where 0 is integrated webcam and 1 is external

for value in getcam:

    current = cv2.VideoCapture(value)
    caplist[current] = value
print(caplist)
# The above code generates a dictionary with key as the name of the current
# stream of video capture with the index from getcam as a value
# the key <VideoCapture 0000017290F2F3B0> is used in the below code as the actual stream
# where as the value is used for the display of which cam is showing , 0 always being the integrated webcam


# for cap in caplist:
while True:

    # cv2.imshow('Camera 1', cap0.read()[1])
    # cv2.imshow('Camera' , cap1.read()[1])

    for cap in caplist:

        # while True:

        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 1, 1)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)

        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for (encodeFace, (top, right, bottom, left)) in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            count = 0
            if matches[matchIndex]:

                name = classRollnos[matchIndex]

                # print(name)
                # y1,x2,y2,x1 = faceLoc
                # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            0.75, (0, 255, 0), 2)

                timelocated(name, cap)

            else:
                name = "Unknown"
                # print(name)

                # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            0.75, (0, 255, 0), 2)

        cv2.imshow(str(caplist.get(cap)), img)
        # cv2.imshow('Webcam', img)
        cv2.waitKey(1)
