#!/usr/bin/env python
# -*- coding: utf-8 -*-

'author Du Xiaogang'

import os
import argparse
import cv2

parser = argparse.ArgumentParser(description='normalize image size to specific size')
parser.add_argument('--image-dir', type=str, required=True,
                    help='the input image data directory')
parser.add_argument('--norm-size',type=int,required=True,
                    help='the input normalize size')                   
args = parser.parse_args()
                    
if args.image_dir is None or not os.path.isdir(args.image_dir):
    print 'please input image dir,check current parameter %s'%args.image_dir
    exit()
if args.norm_size is None:
    print 'please input norm size,check current parameter %s'%args.norm_size
    exit()
    
ext_names = ['.jpg','.jpeg','.png','.bmp']
norm_size = (args.norm_size,args.norm_size)  
image_count = 0;  
for image_root,sub_dirs,file_names in os.walk(args.image_dir):
    file_names.sort()
    for file_name in file_names:
        if os.path.splitext(file_name)[1].lower() in ext_names:
            image_path = os.path.join(image_root,file_name)
            src_image = cv2.imread(image_path)
            if src_image is None:
                continue
            image_count += 1
            if src_image.shape[:2] != norm_size:
                os.remove(image_path)
                src_image = cv2.resize(src_image,norm_size)
                cv2.imwrite(image_path,src_image)

print "image total number is: %d"%image_count