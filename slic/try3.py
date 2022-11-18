#分割出来的超像素块保持在原图的位置

from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy.misc
from PIL import Image
import pandas as pd

# args
args = {"image": 'aaa.png'}

# load the image and apply SLIC and extract (approximately)
# the supplied number of segments
image = cv2.imread(args["image"])
#segments = slic(img_as_float(image), n_segments=100, sigma=5)
slic = cv2.ximgproc.createSuperpixelSLIC(image,cv2.ximgproc.MSLIC,region_size=20,ruler = 20.0)
slic.iterate(10)     #迭代次数，越大效果越好
mask_slic = slic.getLabelContourMask() #获取Mask，超像素边缘Mask==1
label_slic = slic.getLabels()        #获取超像素标签
number_slic = slic.getNumberOfSuperpixels()  #获取超像素数目
mask_inv_slic = cv2.bitwise_not(mask_slic)
# show the output of SLIC
fig = plt.figure('Superpixels')
ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), label_slic))
plt.axis("off")
plt.show()
print("segments:\n", label_slic)
print("np.unique(segments):", np.unique(label_slic))
# loop over the unique segment values
for (i, segVal) in enumerate(np.unique(label_slic)):
    # construct a mask for the segment
    print("[x] inspecting segment {}, for {}".format(i, segVal))
    mask = np.zeros(image.shape[:2], dtype="uint8")
    mask[label_slic == segVal] = 255

    # show the masked region
#   cv2.imshow("Mask", mask)
    img = Image.fromarray(np.multiply(image, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) > 0));
#   cv2.imshow("Applied", np.multiply(image, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) > 0))

    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)

    img.save('./testpic/' + str(i) + '.png')
    cv2.waitKey(0)