from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

radius = 1
n_points = 8
filename=r'./testpic/444.png'
img = cv2.imread(filename)#读图像
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转灰度
lbp = local_binary_pattern(img_gray, n_points, radius)
print(lbp)
# plt.imshow(lbp)