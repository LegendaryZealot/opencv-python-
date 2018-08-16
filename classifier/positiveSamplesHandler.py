import os
import cv2.cv2 as cv

UnprocessedPositiveSamples="./UnprocessedPositiveSamples"
PositiveSamples="./PositiveSamples"
TargetSize=40

def handleImg():
    os.system("rm -f {0}/*".format(PositiveSamples))
    count=1
    for imgFile in os.listdir(UnprocessedPositiveSamples):
        img=cv.imread(os.path.join(UnprocessedPositiveSamples,imgFile))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img=cv.resize(img,(TargetSize,TargetSize),interpolation=cv.INTER_CUBIC)
        cv.imwrite("{0}/{1}.jpg".format(PositiveSamples,count),img)
        count+=1

if __name__ =="__main__":
    handleImg()
    print("DONE!")
else:
    print("BAD~\n")