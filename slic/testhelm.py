import hpelm
import numpy as np
import cv2
import os,re
imglist=[]      #训练数据列表
step=10     #每种照片样本数
type_num=15     #种类数
file_dir='D:\IOFile\YALE'   #照片路径
#读取照片
for tp_num in range(1,type_num+1):
    for st_num in range(1,step+1):
        add_pre=lambda x:'0'+str(x) if len(str(x))==1 else str(x)      #加前缀
        file_path = os.path.join(file_dir, 'subject{}_{}.bmp'.format(add_pre(tp_num),st_num))
        if os.path.isfile(file_path):
            manimg = cv2.resize(cv2.imread(file_path, cv2.IMREAD_GRAYSCALE), (100, 100),
                               interpolation=cv2.INTER_CUBIC)
            manarray=np.array(bytearray(manimg))
            imglist.append(manarray)
#生成ELM
elm=hpelm.ELM(10000,type_num)
#生成训练数据
input_data=[i for i in imglist]
output_data=[]
pos=0
for index in range(0,len(imglist)):
    img_num=int(index/step)      #照片种类编号
    output=[]
    for i in range(type_num):
        if img_num==i:
            output.append(1)
        else:
            output.append(0)
    output_data.append(output)
#添加神经元
elm.add_neurons(30,'lin')
elm.add_neurons(15,'rbf_linf')
#训练
elm.train(np.array(input_data),np.array(output_data))

#测试图片
def predict_photo(photo_num):
    # 准备测试数据
    testim = cv2.resize(cv2.imread(os.path.join(file_dir, 'subject{}_11.bmp'.format(add_pre(photo_num))), cv2.IMREAD_GRAYSCALE), (100, 100),
                        interpolation=cv2.INTER_CUBIC)
    testarray = np.array(bytearray(testim))
    test_data = np.array([testarray.tolist()])
    # 预测
    predict = elm.predict(test_data)
    prbobility = 0  # 照片为某一种类的可能性
    max_photo = 0  # 最可能的照片种类
    for i in range(0, len(predict[0])):
        if prbobility < predict[0][i]:
            prbobility = predict[0][i]
            max_photo = i
    print('该照片最可能属于种类{},概率为{}'.format(max_photo + 1, prbobility))

#测试性能
def test_perfomance():
    true=0
    for num in range(1,16):
        # 读取图片并格式化处理
        im = cv2.resize(cv2.imread(os.path.join(file_dir, 'subject{}_11.bmp'.format(add_pre(num))), cv2.IMREAD_GRAYSCALE), (100, 100),
                            interpolation=cv2.INTER_CUBIC)
        array = np.array(bytearray(im))
        predict=elm.predict(np.array([array.tolist()]))
        prbobility=0
        for i in range(0, len(predict[0])):
            if prbobility < predict[0][i]:
                prbobility = predict[0][i]
                max_photo = i
        if max_photo+1==num:
            true+=1
    print('完成性能测试，正确率为{}'.format(true/15))

if __name__ == '__main__':
    predict_photo(7)
    test_perfomance()