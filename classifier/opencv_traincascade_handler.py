import os

POSINFO="./POSINFO.ini"
NEGINFO="./NEGINFO.ini"
POSCOUNT=5
NEGCOUNT=20
POSIMGSIZE=40
POSPATH="./PositiveSamples"
NEGPATH="./NegativeSamples"
POSVEC="./posvec.vec"
SAMPLECMD="opencv_createsamples -vec {0} -info {1} -num {2} -w {3} -h {4}".format(POSVEC,POSINFO,POSCOUNT,POSIMGSIZE,POSIMGSIZE)
TRAININGCMD="opencv_traincascade -data xml -vec {0} -bg {1} -numPos {2} -numNeg {3} -numStages 10 -w {4} -h {5} -minHitRate 0.999 -maxFalseAlarmRate 0.2 -weightTrimRate 0.95 -featureType LBP".format(POSVEC,NEGINFO,POSCOUNT,NEGCOUNT,POSIMGSIZE,POSIMGSIZE)

def initPosInfo():
    os.system("rm -f {0}".format(POSINFO))
    posImgs=os.listdir(POSPATH)
    with open(POSINFO,"w") as f:
        for posImg in posImgs:
            posImgPath=os.path.join(POSPATH,posImg)
            f.write("{0} 1 0 0 {1} {2}\n".format(posImgPath,POSIMGSIZE,POSIMGSIZE))
    print("init pos info done!")

def initNagInfo():
    os.system("rm -f {0}".format(NEGINFO))
    negImgs=os.listdir(NEGPATH)
    with open(NEGINFO,"w") as f:
        for negImg in negImgs:
            negImgPath=os.path.join(NEGPATH,negImg)
            f.write("{0}\n".format(negImgPath))
    print("init nag info done!")

def startTraincascade():
    os.system("rm -fr xml")
    os.system("mkdir xml")
    print(SAMPLECMD)
    os.system(SAMPLECMD)
    os.system(TRAININGCMD)
    print("done")

if __name__ == "__main__":
    initPosInfo()
    initNagInfo()
    startTraincascade()
else:
    print("bad~")