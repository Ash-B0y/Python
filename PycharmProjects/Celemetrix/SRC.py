import os
from shutil import move
Info = []
f = open("C:/Users/Ash/Desktop/@$h/Input.txt", "r")
for x in f:
    s = x.split("=")
    Info.append(s[1])

for filename in os.listdir(Info[4]):

    if "DSS" in filename:

            move(Info[4]+filename, os.getcwd())
            src = filename
            dst = "NBN_"+src[0:4]+"-"+src[4:6]+"_"+src[15:]
            os.rename(src, dst)
            move(os.getcwd()+"\\"+dst,Info[4])

    if "MTLFN" in filename:

            move(Info[4]+filename, os.getcwd())
            old = filename
            new = old[0:4]+"-"+old[4:6]+"-"+old[6:8]+"-"+old[8:11]+"-"+old[11:]
            os.rename(old, new)
            move(os.getcwd()+"\\"+new, Info[4])