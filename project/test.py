import os
import sys
import numpy as np
from PIL import Image
from feature import glcm_feature as glf
from feature import gabor_feature as gaf
from feature import gray_histogram_feature as grf
from feature import select_organ as so

def writeList2CSV(myList,filePath):
    try:
        file=open(filePath,'w+')
        for items in myList:
            for item in items:
                file.write(str(item))
                # file.write(",")
            file.write("\n")
    except Exception :
        print("数据写入失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭

os.chdir(sys.path[0])
rootdir = './TrainingImg2'
maskdir = './TrainingMask1'
niidirs = os.listdir(rootdir)
f=[]
for niidir in niidirs:
    mpdir = maskdir + '/' + niidir.replace("_0000", "")
    niidir = rootdir + '/' + niidir
    picdirs = os.listdir(niidir)
    for picdir in picdirs:
        maskpic = mpdir + '/' + picdir.replace("png", ".png")
        picdir = niidir + '/' + picdir
        pics = os.listdir(picdir)
        if(np.mean(Image.open(maskpic).convert('L'))==0.0):
            continue
        else:
            print(maskpic)
            index = maskpic.rfind("/")
            page_feature = int(maskpic[index+1:].replace(".png",""))
            # print(page_feature)
            for pic in pics:
                pic = picdir + '/' + pic
                # im1 = pic
                # index = im1.rfind("\\")
                # im1 = im1[0:index]
                # im1 = im1.replace("TrainingImg2", "TrainingMask1")
                # im1 = im1.replace("_0000", "")
                # im1 = im1.replace("png", ".png")
                lable = so.select(pic, maskpic)
                # print(pic, maskpic,lable)
                # if(lable!=0 and lable!=5):
                features = []
                features.extend(glf.glcm_features(pic))
                features.extend(gaf.gabor_features(pic))
                features.extend(grf.gray_features(pic))
                features.append(page_feature)
                features.append(lable)
                f.extend(features)
                print(features)
                #np.savetxt('D:\\python\\project\\new.csv', features, delimiter=',')
writeList2CSV(f,'./project/new.csv')
# np.savetxt('D:\\python\\project\\new.csv', f, delimiter = ',')
#print(so.select('E:\\project\\data\\t2\\TrainingImg2\\train_000_0000\\48png\\514.png','E:\\project\\data\\t2\\TrainingMask1\\train_000\\48.png'))
# im1='E:\\project\\data\\t2\\TrainingImg2\\train_000_0000\\48png\\514.png'
# im2='E:\\project\\data\\t2\\TrainingMask1\\train_000\\48.png'
# print(so.select(im1,im2))
