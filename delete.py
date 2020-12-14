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

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=['ip_address'],username=['name'],password=['passw'])
sftp = ssh_client.open_sftp()


try:
	for entry in sftp.listdir_attr(remote_path):
		timestamp = entry.st_mtime
		createtime = datetime.datetime.fromtimestamp(timestamp)
		now = datetime.datetime.now()
		delta = now - createtime
		if delta.days >= 7:
			filepath = ['remote_path'] + '/' + entry.filename
			filepath2 = ['local_path'] + '/' + entry.filename
			sftp.remove(filepath)
			os.remove(filepath2)
except paramiko.ssh_execption.CouldNotCannonicalize:
	print ('Multiple connection attemps were made and no families succeeded$
	exit (CouldNotCanonicalize)
except paramiko.ssh_execption.AuthenticationException:
	print ('Authentication failed')
	 exit (AuthenticationException)
