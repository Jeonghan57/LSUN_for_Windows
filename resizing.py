# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:18:14 2021

@author: user
"""

import cv2
import os
from tqdm import tqdm

path = "./Dataset/LSUN/Train/LSUN/"
i=0

if not os.path.exists(path):
	os.mkdir(path)
    
for img_name in tqdm(os.listdir(path)):    
    img = cv2.imread(os.path.join(path, img_name))    
    new = cv2.resize(img, dsize=(256, 256), interpolation=cv2.INTER_AREA)    
    cv2.imwrite(path + str(i) + '.png', new)    
    i += 1