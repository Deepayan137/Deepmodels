.. Deep Models in Practice documentation master file, created by
   sphinx-quickstart on Sun Nov 27 22:33:17 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Deep Models in Practice's documentation!
===================================================

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Hello deep learners, welcome to the Deep Models in Practice. Everything around us is growing very rapidly with the advent of new technology. One thing we always keep in mind is :: It's all about making the world a better place:: for us and the coming generation. So this is one of my contributions to make the people life easy by providing the things I learned, that may be from scratch or by building upon gaints. I belive the learning is the process "Learning from Mistakes": Yes we do things and some time they may get wrong, then we notice and learn that is wrong and we are not supposed to do that again. Not only that, I have a lot concepts and ideas to connect and apply to the deep learning field to make it much better and efficient, just one bit less than to the human. I will put a lot of code example which can be easily adapt into your project requirements. Yes there is a lot for you. 

Here is a simple python code to copy 1000 files from one directory to the other directory. We are all very familiar with Kaggle's dogs_vs_cats competetion. Kaggle is open data provider and they conduct amazing comptitions. If you didn't try yet, you must check this out `Kaggle Dog Vs. Cat <https://www.kaggle.com/c/dogs-vs-cats>`. So I downloaded the entire dogs and cats data and I wanted to use a portion of the data set to design a classfier. So here what I did to extract the first 'n' number of images out of one folder and copy to the other.

.. code-block:: python
	:linenos:
	:caption: cp1000.py
	:name: cp1000-py
	# -*- coding: utf-8 -*-


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

	catsT =   '../data/train/cats'  
	catsV =   '../data/validation/cats'  

	dogsT =   '../data/train/dogs'  
	dogsV =   '../data/validation/dogs'

	TRAIN_DIR = '../kaggle/kaggle_dogs_vs_cats/input/train/'
	TEST_DIR = '../kaggle/kaggle_dogs_vs_cats/input/test/'

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
