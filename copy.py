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
local_path = '/home/localuser/Saves'
remote_path = '/home/distantuser/Saves'
ip_address = "192.168.0.2"
name = "distantuser"
passw = "root"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=name,password=passw)
sftp = ssh_client.open_sftp()
scp = SCPClient(ssh_client.get_transport())
scp.put(local_path + "/" + namedir,remote_path)

