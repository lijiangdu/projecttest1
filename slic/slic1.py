import cv2

import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("tmp_upload.jpg")
#初始化slic项，超像素平均尺寸20（默认为10），平滑因子20
slic = cv2.ximgproc.createSuperpixelSLIC(img,cv2.ximgproc.MSLIC,region_size=20,ruler = 20.0)
slic.iterate(10)     #迭代次数，越大效果越好
mask_slic = slic.getLabelContourMask() #获取Mask，超像素边缘Mask==1
label_slic = slic.getLabels()        #获取超像素标签
number_slic = slic.getNumberOfSuperpixels()  #获取超像素数目
mask_inv_slic = cv2.bitwise_not(mask_slic)
img_slic = cv2.bitwise_and(img,img,mask =  mask_inv_slic) #在原图上绘制超像素边界
cv2.imshow("img_slic",img_slic)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img = cv2.imread("tmp_upload.jpg", flags=1)  # 读取彩色图像(BGR)
# imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)  # BGR-HSV 转换
# plt.figure(figsize=(9, 7))
# plt.subplot(221), plt.axis('off'), plt.title("Origin")
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 显示 img1(RGB)
#
# algorithms = [
#     ('SLIC', cv2.ximgproc.SLIC),  # 使用所需的区域大小分割图像
#     ('SLICO', cv2.ximgproc.SLICO),  # 使用自适应紧致因子进行优化
#     ('MSLIC', cv2.ximgproc.MSLIC)]  # 使用流形方法进行优化，产生对内容更敏感的超像素
# region_size = 20
# ruler = 10
# edgeColor = np.ones((img.shape[0], img.shape[1], 3), np.uint8) * 255
# for i in range(3):
#     # 初始化slic项，region_size设置分割图片尺寸大小 ruler设置平滑因子
#     slic = cv2.ximgproc.createSuperpixelSLIC(imgHSV, algorithms[i][1], region_size, float(ruler))
#     slic.iterate(5)  # 迭代次数，默认 10 次
#     slic.enforceLabelConnectivity(100)  # 最小尺寸
#     mask_slic = slic.getLabelContourMask()  # 获取Mask，超像素边缘Mask==1
#     mask_color = np.array([mask_slic for i in range(3)]).transpose(1, 2, 0)  # 转为 3通道
#     img_slic = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask_slic))  # 在原图上绘制超像素边界
#
#     plt.subplot(2, 2, i + 2), plt.axis('off'), plt.title("Slic ({})".format(algorithms[i][0]))
#     plt.imshow(cv2.cvtColor(img_slic, cv2.COLOR_BGR2RGB))
#
# plt.tight_layout()
# plt.show()

# from skimage.segmentation import slic
# from skimage.segmentation import mark_boundaries
# from skimage.util import img_as_float
# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
# import scipy.misc
# from PIL import Image
#
# # args
# args = {"image": 'tmp_upload.jpg'}
#
# # load the image and apply SLIC and extract (approximately)
# # the supplied number of segments
# image = cv2.imread(args["image"])
# #segments = slic(img_as_float(image), n_segments=100, sigma=5)
# slic = cv2.ximgproc.createSuperpixelSLIC(image,cv2.ximgproc.MSLIC,region_size=20,ruler = 20.0)
# slic.iterate(10)     #迭代次数，越大效果越好
# mask_slic = slic.getLabelContourMask() #获取Mask，超像素边缘Mask==1
# label_slic = slic.getLabels()        #获取超像素标签
# number_slic = slic.getNumberOfSuperpixels()  #获取超像素数目
# mask_inv_slic = cv2.bitwise_not(mask_slic)
# # show the output of SLIC
# fig = plt.figure('Superpixels')
# ax = fig.add_subplot(1, 1, 1)
# ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), label_slic))
# plt.axis("off")
# plt.show()
# print("segments:\n", label_slic)
# print("np.unique(segments):", np.unique(label_slic))
# # loop over the unique segment values
# for (i, segVal) in enumerate(np.unique(label_slic)):
#     # construct a mask for the segment
#     print("[x] inspecting segment {}, for {}".format(i, segVal))
#     mask = np.zeros(image.shape[:2], dtype="uint8")
#     mask[label_slic == segVal] = 255
#
#     # show the masked region
#     cv2.imshow("Mask", mask)
#     img = Image.fromarray(np.multiply(image, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) > 0));
#     cv2.imshow("Applied", np.multiply(image, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) > 0))
#     img.save(str(i) + '.png')
#     cv2.waitKey(0)