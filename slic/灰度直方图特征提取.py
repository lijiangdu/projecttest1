import glob
import os
from matplotlib import pyplot as plt
import cv2
import numpy as np

# #方法1：直方图数据计算统计
# def gray_features(img):
#     hist = cv2.calcHist([img],[0],None,[256],[0,255])#得到全局直方图统计数据
#     h,w = img.shape
#     hist = hist/(h*w)#将直方图归一化为0-1，概率的形式
#
#     grayFeature = []
#     #灰度平均值
#     mean_gray = 0
#     for i in range(len(hist)):
#         mean_gray += i*hist[i]
#     grayFeature.append(mean_gray[0])
#
#     #灰度方差
#     var_gray = 0
#     for i in range(len(hist)):
#         var_gray += hist[i]*((i - mean_gray)**2)
#     grayFeature.append(var_gray[0])
#
#     #能量sum(hist[i])**2
#     ##归一化
#     max_ = np.max(hist)
#     min_ = np.min(hist)
#     histOne = (hist - min_)/(max_ - min_)
#     ##求解能量
#     energy = 0
#     for i in range(len(histOne)):
#         energy += histOne[i]**2
#     grayFeature.append(energy[0])
#
#     #熵
#     he = 0
#     for i in range(len(hist)):
#         if hist[i] != 0:#当等于0时，log无法进行计算，因此只需要计算非0部分的熵即可
#             he += hist[i]*(np.log(hist[i])/(np.log(2)))
#     he = -he
#     grayFeature.append(he[0])#因为返回的是含有一个元素的数组，所以通过取值操作将其取出来再加入到列表中去
#
#     #灰度对比度
#     con = np.max(img)-np.min(img)
#     grayFeature.append(con)
#     return grayFeature
#
# #顺序遍历result文件夹下的图片的路径
# WSI_MASK_PATH = 'testpic'#存放图片的文件夹路径
# paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.png'))
# paths.sort(key=lambda x:int(x.split('.')[0].split('\\')[1]))
#
# for path in paths:
#     #超像素块位置
#     img = cv2.imread(str(path),0)
#     grayFeas = gray_features(img)
#     print(str(path) + ": " + str(grayFeas))
#     print("-------------------------------------------------------------------------------------")

#方法2：直方图
# #参数0表示以灰度图像读入该图片，也就是说在读取的同时就进行了处理
# img = cv2.imread('testpic/300.png', 0)
# img1 = cv2.imread('testpic/173.png', 0)
# img2 = cv2.imread('testpic/174.png', 0)
# #得到全局直方图统计数据
# hist = cv2.calcHist([img],[0],None,[256],[0,255])
# hist = hist[1:256] #去除0(背景黑色)
# print(hist)
# #灰度向量对比函数
# hist1 = cv2.calcHist([img1],[0],None,[256],[0,255])
# hist2 = cv2.calcHist([img2],[0],None,[256],[0,255])
# hist1 = hist1[1:256]
# hist2 = hist2[1:256]
# # 输出列表
# print(cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL))
# for i in range(len(hist)):
#     print(str(i) + " :" + str(hist[i]))
# #显示(cv2的方法)
# plt.plot(hist,color='y')
# plt.plot(hist1,color='b')
# plt.plot(hist2,color='r')
# plt.show()

#方法2：直方图
#顺序遍历result文件夹下的图片的路径，source_path为超像素块图片的文件夹路径
def gray_features(source_path):
    WSI_MASK_PATH = source_path #存放图片的文件夹路径
    paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.png')) #读取图片的路径
    paths.sort(key=lambda x:int(x.split('.')[0].split('\\')[1])) #排序

    #f = open("temp.txt", "w")
    for path in paths:
        # 参数0表示以灰度图像读入该图片，也就是说在读取的同时就进行了处理
        img = cv2.imread(str(path),0)
        hist = cv2.calcHist([img],[0],None,[256],[0,255])   #读取灰度矩阵，cv2.calcHist为简单的灰度直方图比较方法
        hist = hist[1:256] #去除0(背景黑色)
        #f.write(str(hist) + '\n')
    #f.close()
    return hist

#测试执行
# gray_features('testpic')