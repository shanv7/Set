#!/usr/bin/env python


import keras
import os

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
                             rotation_range=40,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest')

dirList = os.listdir("train/")
for tdir in dirList:
    fname = tdir
    if "." not in tdir:
        imgpath = 'train/'+tdir+'/'+tdir+'.jpg'
        print imgpath
        img = load_img(imgpath)  # this is a PIL image
        x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the `preview/` directory
        i = 0
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir='train/'+tdir, save_prefix='GDE1', save_format='jpeg'):
            i += 1
            if i > 10:
                break  # otherwise the generator would loop indefinitely
