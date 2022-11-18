import numpy as np
import cv2
import matplotlib.pyplot as plt
__all__ = [cv2]

def qvzao(filename):
    image=cv2.imread(filename)
    dst=cv2.bilateralFilter(src=image,d=0,sigmaColor=600,sigmaSpace=1)
    # cv2.namedWindow('qvzao',0)
    # cv2.resizeWindow('qvzao',512,512)
    # cv2.imshow("qvzao",dst)
    # cv2.waitKey(0)
    cv2.imwrite(filename, dst)

# src=cv2.imread(r'E:\\project\\data\\t2\\11\\train_005_0000\\1.png')
# # qvzao('E:\\project\\data\\t2\\11\\train_005_0000\\1.png')
# cv2.namedWindow('src', 0)
# cv2.resizeWindow('src', 512, 512)
# cv2.imshow('src',src)
# cv2.waitKey(0)