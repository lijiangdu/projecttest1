import numpy as np
from PIL import Image
def select(hyperpixelfile,labalfile):
    image1 = Image.open(hyperpixelfile)
    im_gray1 = image1.convert('L')
    im1 = np.array(im_gray1)
    # for i in im:
    #     print(i)
    # a= set()
    # for ms in im:
    #     for m in ms:
    #         a.add(m)
    # print(a)
    b = []
    for index, x in np.ndenumerate(im1):
        if x != 0:
            b.append(index)
    # print(b)
    image2 = Image.open(labalfile)
    im_gray2 = image2.convert('L')
    im2 = np.array(im_gray2)
    # a= set()
    # for ms in im2:
    #     for m in ms:
    #         a.add(m)
    # print(a)
    c = [0, 0, 0, 0, 0, 0]
    for i in b:
        if im2[i] == 0:
            c[0] += 1
        elif (im2[i] == 64):
            c[1] += 1
        elif im2[i] == 127:
            c[2] += 1
        elif im2[i] == 191:
            c[3] += 1
        elif im2[i] == 255:
            c[4] += 1
        else:
            c[5] += 1
    print(c.index(max(c)))