#!/usr/bin/env python3

import sys #pour les arguments
import time #pour date les sauvegardes
import datetime
import shutil #copy and del des fichiers
import os #Create dir and del
import tarfile
import paramiko
from scp import SCPClient
from datetime import timedelta

dailydir = time.strftime("%Y%m%d")
namedir = "Sauvegardedu" + dailydir + ".tar"
local_path = '/home/localuser/Saves

try:
	 with  tarfile.open (local_path + "/" + namedir, 'w') as archive:
		archive.add ('/var/www/html')
except tarfile.CompressionError:
	print ('CompressionError')
	exit (Compression)
except tarfile.tarError:
	print ('tarError reload the script')
	exit(tarError)

