# # 遍历文件夹
# import os
# # nii格式一般都会用到这个包
# import nibabel as nib
# # 转换成图像
# import imageio
# import numpy as np
# import cv2
# import PIL.Image as pimg
#
#
# # 主函数
# def nii_to_image(filepath,imgfile):
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
#             col = x
#             for m in silce:
#                 for j in range(col // 2):
#                     m[j], m[col - 1 - j] = m[col - 1 - j], m[j]
#             # silce= silce.transpose(pimg.FLIP_LEFT_RIGHT)
#             # 保存图像
#             imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce)

# 遍历文件夹
import os
# nii格式一般都会用到这个包
import nibabel as nib
# 转换成图像
import imageio
import numpy as np
import cv2
import PIL.Image as pimg

# 主函数
def nii_to_image(filepath,imgfile):
    # 读取nii文件夹
    filenames = os.listdir(filepath)

    # 开始读取nii文件
    for f in filenames:
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # 读取nii
        img_fdata = img.get_fdata()
        # 去掉nii的后缀名
        fname = f.replace('.nii', '')
        img_f_path = os.path.join(imgfile, fname)

        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_f_path):
            # 新建文件夹
            os.makedirs(img_f_path)

            # 开始转换为图像
        (x, y, z) = img.shape
        # z是图像的序列
        for i in range(z):
            # 选择哪个方向的切片都可以
            silce = img_fdata[:, :, i]
            silce = np.rot90(silce)
            col = x
            for m in silce:
                for j in range(col // 2):
                    m[j], m[col - 1 - j] = m[col - 1 - j], m[j]
            # silce= silce.transpose(pimg.FLIP_LEFT_RIGHT)
            # 保存图像
            imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce)