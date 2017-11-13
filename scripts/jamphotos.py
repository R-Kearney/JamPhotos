import os, sys
import time

#Keep checking for new files into the Dropbox Camera folder

path = "/root/Dropbox/Camera Uploads/"

old_files = []

while(1):
	time.sleep(.2)
	new_files = os.listdir( path )
	if new_files != old_files:
		for file in new_files:
			if file not in old_files:
				new_file = file

				print(new_file)
			
		#do the thraining things

				old_files.append(new_file)
