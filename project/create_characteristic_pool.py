import os
from pretreatment import nii_png
from pretreatment import Bilateral_filtering as bf
from pretreatment import mslic
#26
trainnii='E:\\project\\data\\t2\\TrainingImg'
masknii='E:\\project\\data\\t2\\TrainingMask'
trainpng='E:\\project\\data\\t2\\TrainingImg1'
maskpng='E:\\project\\data\\t2\\TrainingMask1'
segments='E:\\project\\data\\t2\\TrainingImg2\\train_000_0000\23png'
#将nii转换成png格式
# nii_png.nii_to_image(trainnii,trainpng)
# nii_png.nii_to_image(masknii,maskpng)
#双边滤波去噪
# dirs = os.listdir(trainpng)
# for dir in dirs:
#     dir = trainpng+"\\"+dir
#     # print(dir)
#     files = os.listdir(dir)
#     for f in files:
#         f=dir+"\\"+f
#         # print(f)
#         bf.qvzao(f)

#超像素块切割
dirs = os.listdir(trainpng)
for dir in dirs:
    dir = trainpng+"\\"+dir
    dir2=dir.replace("TrainingImg1","TrainingImg2")
    # print(dir)
    # print(dir2)
    files = os.listdir(dir)
    for f in files:
        dir1=dir+"\\"+f
        dir3=dir2+"\\"+f.replace(".png","png")
        # print(dir1)
        # print(dir3)
        mslic.mslic(dir1,dir3)
        print(dir3 + "已完成")