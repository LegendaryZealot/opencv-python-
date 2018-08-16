import cv2.cv2 as cv

print("loading cascade")
# faceCascade = cv.CascadeClassifier("./xml/cascade.xml")
faceCascade = cv.CascadeClassifier("./haarcascade_frontalface_default.xml")
print("loaded cascade")

cap = cv.VideoCapture(0)
flag = 0
timeF = 10
while True:
    flag+=1
    ret, frame = cap.read()
    img = frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rect = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=3,
        minSize=(3,3),
        flags = cv.IMREAD_GRAYSCALE
    )
    for (x, y, w, h) in rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('frame', frame)
    cv.waitKey(1)
cap.release()
cv.destroyAllWindows()
cv.destroyAllWindows()