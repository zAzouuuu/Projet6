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

def create(vars):

try:
	 with  tarfile.open (vars['local_path'] + "/" + vars['namedir'], 'w') as archive:
		archive.add vars['save_path']
except tarfile.CompressionError:
	print (0)
	exit (Compression)
except tarfile.tarError:
	print (1)
	exit(tarError)

