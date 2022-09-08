import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
# %matplotlib inline 
import matplotlib.pyplot as plt
import os
# print(os.listdir("captcha_images_v2"))

# Any results you write to the current directory are saved as output.

from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras import callbacks
import os
import cv2
import string
import numpy as np

symbols = string.ascii_lowercase + "0123456789" + string.ascii_uppercase 
model = load_model('originModel.h5')


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
    # print("filepath in predict:" + filepath)
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (200, 50))
    if img is not None:
        img = img / 255.0
    else:
        print("Not detected")
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))
        #probs.append(np.max(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
        # print("capt: " + capt)
    return capt[:4]#, sum(probs) / 5

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