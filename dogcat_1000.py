# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import glob
import os
import re
import shutil 

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import PIL
from PIL import Image

def natural_key(string_):
    """
    Define sort key that is integer-aware
    """
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]
catsT =   '/users/shravankumar/deeplearning/Pyscripts/temp/data/train/cats'  
catsV =   '/users/shravankumar/deeplearning/Pyscripts/temp/data/validation/cats'  

dogsT =   '/users/shravankumar/deeplearning/Pyscripts/temp/data/train/dogs'  
dogsV =   '/users/shravankumar/deeplearning/Pyscripts/temp/data/validation/dogs'

TRAIN_DIR = '/users/shravankumar/kaggle/kaggle_dogs_vs_cats/input/train/'
TEST_DIR = '/users/shravankumar/kaggle/kaggle_dogs_vs_cats/input/test/'

train_cats = sorted(glob.glob(os.path.join(TRAIN_DIR, 'cat*.jpg')), key=natural_key)
train_dogs = sorted(glob.glob(os.path.join(TRAIN_DIR, 'dog*.jpg')), key=natural_key)
train_all = train_cats + train_dogs

test_all = sorted(glob.glob(os.path.join(TEST_DIR, '*.jpg')), key=natural_key)

train_images = train_dogs[:1000] + train_cats[:1000]

cats_tr = train_cats[:1000]
cats_vl = train_cats[1000:1400]

dogs_tr = train_dogs[:1000]
dogs_vl = train_dogs[1000:1400]

#for i,fname in enumerate(cats_tr):
#    print(fname)
#    if i >10:
#        break
#    
#for i,fname in enumerate(cats_tr):
#    print(fname)
#    shutil.copy(fname,catsT)
#
#for i,fname in enumerate(cats_vl):
#    print(fname)
#    shutil.copy(fname,catsV)
#    
#for i,fname in enumerate(dogs_tr):
#    print(fname)
#    shutil.copy(fname,dogsT)
#
#for i,fname in enumerate(dogs_vl):
#    print(fname)
#    shutil.copy(fname,dogsV)

train_cats1 = sorted(glob.glob(os.path.join(catsT, 'cat*.jpg')), key=natural_key)
train_dogs1 = sorted(glob.glob(os.path.join(dogsT, 'dog*.jpg')), key=natural_key)   

val_cats1 = sorted(glob.glob(os.path.join(catsV, 'cat*.jpg')), key=natural_key)
val_dogs1 = sorted(glob.glob(os.path.join(dogsV, 'dog*.jpg')), key=natural_key) 
