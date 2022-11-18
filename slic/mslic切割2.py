#分割出的碎片使用最小矩阵分成一个个单独的图片

import skimage
from skimage.segmentation import slic,mark_boundaries
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import numpy as np
import cv2
#
# np.set_printoptions(threshold=np.inf)
img_name = '222.tif'
img = cv2.imread(img_name) #as_gray是灰度读取，得到的是归一化值
#segments = slic(img, n_segments=10, compactness=0.2,start_label = 1)#进行SLIC分割
slic = cv2.ximgproc.createSuperpixelSLIC(img,cv2.ximgproc.MSLIC,region_size=20,ruler = 20.0)
slic.iterate(5)     #迭代次数，越大效果越好
mask_slic = slic.getLabelContourMask() #获取Mask，超像素边缘Mask==1
label_slic = slic.getLabels()        #获取超像素标签
number_slic = slic.getNumberOfSuperpixels()  #获取超像素数目
mask_inv_slic = cv2.bitwise_not(mask_slic)
# out=mark_boundaries(img,segments)
# out = out*255 #io的灰度读取是归一化值，若读取彩色图片去掉该行
# img3 = Image.fromarray(np.uint8(out))
# img3.show()
# seg_img_name = 'seg.png'
# img3.save(seg_img_name)#显示并保存加上分割线后的图片
img_slic = cv2.bitwise_and(img,img,mask =  mask_inv_slic) #在原图上绘制超像素边界
cv2.imshow("img_slic",img_slic)
cv2.waitKey(0)
cv2.destroyAllWindows()

maxn = max(label_slic.reshape(int(label_slic.shape[0] * label_slic.shape[1]), ))
for i in range(1, maxn + 1):
    # ##### 保存灰度图片的部分，as_gray=True
    # a = np.array(label_slic == i)
    # b = img * a
    # w, h = [], []
    # for x in range(b.shape[0]):
    #     for y in range(b.shape[1]):
    #         if b[x][y] != 0:
    #             w.append(x)
    #             h.append(y)
    #
    # c = b[min(w):max(w), min(h):max(h)]
    # c = c * 255
    # d = c.reshape(c.shape[0], c.shape[1], 1)
    # e = np.concatenate((d, d), axis=2)
    # e = np.concatenate((e, d), axis=2)
    # ###########
    # '''
    ##### 保存彩色图片的部分，as_gray=True
    a = np.array(label_slic == i)
    a = a.reshape(a.shape[0],a.shape[1],1)
    a1 = np.concatenate((a,a),axis=2)
    a = np.concatenate((a1, a), axis=2)
    b = img * a
    w,h = [],[]
    for x in range(b.shape[0]):
        for y in range(b.shape[1]):
            if b[x][y][0] != 0:
                w.append(x)
                h.append(y)
    c = b[min(w):max(w),min(h):max(h)]
    e = c.reshape(c.shape[0],c.shape[1],3)
    # ###################
    # '''
    img2 = Image.fromarray(np.uint8(e))
    img2.save(str(i) + '.png')
    print('已保存第' + str(i) + '张图片')