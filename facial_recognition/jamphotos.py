import os, sys, shutil
import time
import argparse
from subprocess import *

from align.align_dataset_mtcnn import main as align


photos_path = "/root/Dropbox/Camera Uploads/"
new_photos = "/var/www/jamphotos/facial_recognition/new_photos/"
aligned_photos = "/var/www/jamphotos/facial-recognition/aligned_photos/"

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir')
parser.add_argument('--output_dir')
parser.add_argument('--image-size', type=int)
parser.add_argument('--margin', type=int)
parser.add_argument('--random-order')
parser.add_argument('--gpu-memory-fraction', type=float)
parser.add_argument('--has_classes')
parser.add_argument('--no-classes')
align_args = parser.parse_args(['--input_dir', '\'/var/www/jamphotos/facial_recognition/new_photos\'', '--output_dir', '\'/var/www/jamphotos/facial_recognition/aligned_photos\''
 ,'--image-size', '182', '--margin', '44', '--random-order', 'True', '--gpu-memory-fraction', '1.0', '--no-classes', 'True', '--has_classes', 'False' ])


old_files = []

#Keep checking for new files into the Dropbox Camera folder
while(1):
	time.sleep(.2)
	new_files = os.listdir( photos_path )
	if new_files != old_files:
		for file in new_files:
			if file not in old_files:
				path = os.path.join(photos_path, file)
				shutil.copy(path, new_photos)
				
				align(align_args)			
				#do the thraining things

				old_files.append(file)

