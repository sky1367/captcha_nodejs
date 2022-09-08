import numpy as np
import pandas as pd   #三民+聯合
import matplotlib.pyplot as plt
import os
# print(os.listdir("captcha_images_v2"))


from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras import callbacks
import os
import cv2
import string
import numpy as np

#Init main values
symbols ="0123456789" # All symbols captcha can contain
num_symbols = len(symbols)
print(num_symbols)
img_shape = (50, 200, 1)
model = load_model('newModel_900.h5')


# 取的img內最新建立的照片
# dir = r"C:\Users\Student\Downloads\upload-main\public\img"
# dir = r"C:\Users\Student\Desktop\captcha_nodejs\public\img"
# file_lists = os.listdir(dir)
# file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
# if not os.path.isdir(dir + "\\" + fn) else 0)
# file = os.path.join(dir, file_lists[-1])
# filepath = file
# filepath = r"C:\Users\Student\Desktop\captcha_nodejs\public\img\2bg48.png"
dir = r"C:\Users\Student\Desktop\captcha_nodejs\public\img"
file_lists = os.listdir(dir)
file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
if not os.path.isdir(dir + "\\" + fn) else 0)
file = os.path.join(dir, file_lists[-1])
filepath = file
print("filepath in py:" + filepath)


def predict(filepath):
    img = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    img = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)[1]
    img = cv2.erode(img, None, iterations=1)
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    if img is not None:
        img = cv2.resize(img, (200,50))
        img = img / 255.0
#         img = np.reshape(img, (50, 200, 1))
    else:
        print("Not detected")
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (4, 10)) #4個字 0-9
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))
        #probs.append(np.max(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
    return capt#, sum(probs) / 5

# img=cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
# plt.imshow(img, cmap=plt.get_cmap('gray'))
print("Predicted Captcha =",predict(filepath))



if __name__ == '__main__':
    # dir = r"C:\Users\Student\Desktop\captcha_nodejs\public\img"
    # file_lists = os.listdir(dir)
    # file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
    # if not os.path.isdir(dir + "\\" + fn) else 0)
    # file = os.path.join(dir, file_lists[-1])
    # filepath = file
    data = predict(filepath)
    # print(data)