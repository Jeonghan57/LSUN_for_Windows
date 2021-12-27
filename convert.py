# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:16:34 2021

@author: user
"""

from tqdm import tqdm
import argparse
import cv2
import os

parser = argparse.ArgumentParser()
parser.add_argument('--indir', help = "The path of the flat folder")
parser.add_argument('--outdir', help = "The path of the output folder")
args = parser.parse_args()

if not os.path.exists(args.outdir):
	os.mkdir(args.outdir)
for img_name in tqdm(os.listdir(args.indir)):
	img = cv2.imread(os.path.join(args.indir, img_name))
	cv2.imwrite(os.path.join(args.outdir, img_name[:-5] + '.png'), img)