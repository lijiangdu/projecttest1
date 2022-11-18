# import math
# import cv2
# import numpy as np
# from skimage import filters
#
#
# filename=r'testpic/78.png'
# img = cv2.imread(filename)#读图像
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转灰度
# frequency=[0.1,1,2,3,4]
# theta=[0,math.pi/8,math.pi/4,math.pi/8*3,math.pi/2,math.pi/4*5,math.pi/2*3,math.pi/7*11]
# #gabor变换
# for f in frequency:
#     for t in theta:
#         real, imag = filters.gabor(img_gray, frequency=f, theta=t, n_stds=5)
#         # 取模
#         img_mod = np.sqrt(real.astype(float) ** 2 + imag.astype(float) ** 2)
#         # 图像缩放（下采样）
#         newimg = cv2.resize(img_mod, (0, 0), fx=1 / 4, fy=1 / 4, interpolation=cv2.INTER_AREA)
#         tempfea = newimg.flatten()  # 矩阵展平
#         tmean = np.mean(tempfea)  # 求均值
#         tstd = np.std(tempfea)  # 求方差
#         newfea = (tempfea - tmean) / tstd  # 数值归一化
#         print(newfea)


#gabor纹理特征提取
import cv2
import numpy as np
from skimage import filters

# 参数是图片地址，返回值是[均值，方差]
def gabor_features(filename):
    img = cv2.imread(filename)#读图像
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转灰度
    frequency=0.6
    #gabor变换
    real, imag = filters.gabor(img_gray, frequency=0.6,theta=45,n_stds=5)
    #取模
    img_mod=np.sqrt(real.astype(float)**2+imag.astype(float)**2)
    #图像缩放（下采样）
    newimg = cv2.resize(img_mod,(0,0),fx=1/4,fy=1/4,interpolation=cv2.INTER_AREA)
    tempfea = newimg.flatten()#矩阵展平
    tmean = np.mean(tempfea)#求均值
    tstd = np.std(tempfea)#求方差
    # if tstd == 0:
    #     return 0
    #newfea = (tempfea - tmean)/tstd#数值归一化
    newfea = []
    newfea.append(tmean)
    newfea.append(tstd)
    return newfea

# print(gabor_features('testpic/78.png'))
# print(gabor_features('testpic/89.png'))
# print(gabor_features('testpic/9.png'))
# print(gabor_features('testpic/69.png'))
# print(gabor_features('testpic/39.png'))