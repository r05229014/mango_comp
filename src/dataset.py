import os 
import shutil
import pandas as pd

df = pd.read_csv('../dataset/dev.csv', header=None)
train_folder = '../dataset/C1-P1_Train'
dev_folder = '../dataset/C1-P1_Dev'

train_dst = '../dataset/train/'
dev_dst = '../dataset/dev/'
for index, row in df.iterrows():
    name, label = row[0], row[1]
    src = os.path.join(dev_folder, name)
    dst = os.path.join(dev_dst, label, name)
    shutil.copy(src, dst)

