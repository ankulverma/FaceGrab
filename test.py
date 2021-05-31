index = 0
arr = []

import cv2

while index < 100:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1


print(arr)
