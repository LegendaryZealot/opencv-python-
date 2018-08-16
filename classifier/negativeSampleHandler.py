import os
import cv2.cv2 as cv

UnprocessedNegativeSamples="./UnprocessedNegativeSamples"
NegativeSamples="./NegativeSamples"
TargetSize=40

def handleImg():
    os.system("rm -f {0}/*".format(NegativeSamples))
    count=1
    for imgFile in os.listdir(UnprocessedNegativeSamples):
        img=cv.imread(os.path.join(UnprocessedNegativeSamples,imgFile))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # img=cv.resize(img,(TargetSize,TargetSize),interpolation=cv.INTER_CUBIC)
        cv.imwrite("{0}/{1}.jpg".format(NegativeSamples,count),img)
        count+=1

if __name__ =="__main__":
    handleImg()
    print("DONE!")
else:
    print("BAD~\n")