import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImageSourceDirectory'
images = []
classRollnos = []
myList = os.listdir(path)
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


def timelocated(name, cap):
    with open('TimeLocated.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = {}

        for line in myDataList:
            entry = line.split(',')
            nameList.update({entry[0]: entry[0]})

        res = False
        for key in nameList:
            if nameList[key] == cap:
                res = True
                break

        if res == False and count < 4:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}  ,  {dtString}  ,  {str(caplist.get(cap))} ')


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

                name = classRollnos[matchIndex].upper()

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
