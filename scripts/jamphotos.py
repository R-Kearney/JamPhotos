import os, sys
import time
from subprocess import *
from align.align_dataset_mtcnn import main as align

#Keep checking for new files into the Dropbox Camera folder

path = "/root/Dropbox/Camera Uploads/"
align_args = ['input_dir', '/var/www/jamphotos/scripts/tmp', 'output_dir', '/var']

old_files = []

while(1):
	time.sleep(.2)
	new_files = os.listdir( path )
	if new_files != old_files:
		for file in new_files:
			if file not in old_files:
				new_file = file
				full_path = path+new_file
				print(full_path)
				align(full_path)
				#do the thraining things

				old_files.append(new_file)
