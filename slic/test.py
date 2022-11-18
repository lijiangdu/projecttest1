# import nii_png
# nii_png.nii_to_image('E:\\project\\data\\t2\\1','E:\\project\\data\\t2\\11')
# 遍历文件夹
# import os
# # nii格式一般都会用到这个包
# import nibabel as nib
# # 转换成图像
# import imageio
# import numpy as np
#
#
# # 主函数
# def nii_to_image(filepath):
#     # 读取nii文件夹
#     filenames = os.listdir(filepath)
#
#     # 开始读取nii文件
#     for f in filenames:
#         img_path = os.path.join(filepath, f)
#         img = nib.load(img_path)  # 读取nii
#         img_fdata = img.get_fdata()
#         # 去掉nii的后缀名
#         fname = f.replace('.nii', '')
#         img_f_path = os.path.join(imgfile, fname)
#
#         # 创建nii对应的图像的文件夹
#         if not os.path.exists(img_f_path):
#             # 新建文件夹
#             os.makedirs(img_f_path)
#
#             # 开始转换为图像
#         (x, y, z) = img.shape
#         # z是图像的序列
#         for i in range(z):
#             # 选择哪个方向的切片都可以
#             silce = img_fdata[:, :, i]
#             silce = np.rot90(silce)
#             # 保存图像
#             imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce)
#
# import nii_png
# filepath = "E:\\project\\data\\t2\\1"
# imgfile = "E:\\project\\data\\t2\\11"
# nii_png.nii_to_image(filepath,imgfile)

# import numpy as np
# import os  # 遍历文件夹
# import nibabel as nib  # nii格式一般都会用到这个包
# import imageio  # 转换成图像
# import PIL.Image as pimg
#
# def nii_to_image(niifile):
#     filenames = os.listdir(filepath)  # 读取nii文件夹
#     slice_trans = []
#
#     for f in filenames:
#         # 开始读取nii文件
#         img_path = os.path.join(filepath, f)
#         img = nib.load(img_path)  # 读取nii
#         img_fdata = img.get_fdata()
#         fname = f.replace('.nii', '')  # 去掉nii的后缀名
#         img_f_path = os.path.join(imgfile, fname)
#         # 创建nii对应的图像的文件夹
#         if not os.path.exists(img_f_path):
#             os.mkdir(img_f_path)  # 新建文件夹
#
#         # 开始转换为图像
#         (x, y, z) = img.shape
#         for i in range(z):  # z是图像的序列
#             silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
#             silce = np.rot90(silce)
#             col = x
#             for m in silce:
#                 for j in range(col // 2):
#                     m[j], m[col - 1 - j] = m[col - 1 - j], m[j]
#             imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce)
#             # im = img.open(img_f_path+"//"+'{}.png'.format(i))
#             # ng = im.transpose(img.FLIP_LEFT_RIGHT)  # 左右对换。
#             # 保存图像
#
#
# if __name__ == '__main__':
#     filepath = 'E:\\project\\data\\t2\\1'
#     imgfile = 'E:\\project\\data\\t2\\1'
#     nii_to_image(filepath)
# import 双边滤波去噪 as bs
# bs.qvzao('E:\\project\\data\\t2\\11\\train_005_0000\\13.png')
# import mslic切割 as mslic
# mslic.mslic('E:\\project\\data\\t2\\TrainingImg1\\train_000_0000\\23.png','E:\\project\\data\\t2\\TrainingImg2\\train_000_0000\\23png')
#0, 64, 255, 127, 191
import numpy as np
# from PIL import Image
# image1=Image.open('E:\\project\\data\\t2\\TrainingImg2\\train_000_0000\\48png\\662.png')
# im_gray1 = image1.convert('L')
# im1 = np.array(im_gray1)
# # for i in im:
# #     print(i)
# # a= set()
# # for ms in im:
# #     for m in ms:
# #         a.add(m)
# # print(a)
# b=[]
# for index, x in np.ndenumerate(im1):
#     if x!=0 :
#         b.append(index)
# # print(b)
# image2=Image.open('E:\\project\\data\\t2\\TrainingMask1\\train_000\\48.png')
# im_gray2 = image2.convert('L')
# im2 = np.array(im_gray2)
# # a= set()
# # for ms in im2:
# #     for m in ms:
# #         a.add(m)
# # print(a)
# c=[0,0,0,0,0,0]
# for i in b:
#     if im2[i] == 0:
#         c[0]+=1
#     elif (im2[i] ==64):
#         c[1]+=1
#     elif im2[i]==127 :
#         c[2]+=1
#     elif im2[i]==191:
#         c[3]+=1
#     elif im2[i]==255:
#         c[4]+=1
#     else:
#         c[5]+=1
# print(c.index(max(c)))
import select_organ as so
im1='E:\\project\\data\\t2\\TrainingImg2\\train_000_0000\\48png\\514.png'
im2='E:\\project\\data\\t2\\TrainingMask1\\train_001\\102.png'
# so.select(im1,im2)
# import 灰度直方特征提取统计 as hui
# print(hui.gray_features(im1))
# index = im1.rfind("\\")
# im1=im1[0:index]
# im1=im1.replace("TrainingImg2","TrainingMask1")
# im1=im1.replace("_0000","")
# im1=im1.replace("png",".png")
# print(im1)
# from PIL import Image
# print(np.mean(Image.open(im2).convert('L')))
def writeList2CSV(myList,filePath):
    try:
        file=open(filePath,'w+')
        for items in myList:
            for item in items:
                file.write(str(item))
                file.write(",")
            file.write("\n")
    except Exception :
        print("数据写入失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭
list = [[1.1,2.3,3],[3,4,5],[5,6,7]]
list1 = [1.9484848,2.4844894,3.58845418,48,9.48484]
writeList2CSV(list,'D:\\python\\project\\new.csv')