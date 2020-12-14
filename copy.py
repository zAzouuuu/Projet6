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

def connect(vars):
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=vars['ip_address'],username=vars['name'],password=vars['passw'])
  return (ssh_client)

def copy(handle_ssh, vars):
  scp = SCPClient(handle_ssh.get_transport())
  scp.put(vars['local_path'] + "/" + vars['namedir'],vars['remote_path'])


def delete(handle_ssh, vars):
sftp = handle_ssh.open_sftp()

try:
        for entry in sftp.listdir_attr(remote_path):
                timestamp = entry.st_mtime
                createtime = datetime.datetime.fromtimestamp(timestamp)
                now = datetime.datetime.now()
                delta = now - createtime
                if delta.days >= 7:
                        filepath = vars['remote_path'] + '/' + entry.filename
                        filepath2 = vars['local_path'] + '/' + entry.filename
                        sftp.remove(filepath)
                        os.remove(filepath2)
except paramiko.ssh_execption.CouldNotCannonicalize:
        print ('Multiple connection attemps were made and no families succeeded$
        exit (CouldNotCanonicalize)
except paramiko.ssh_execption.AuthenticationException:
        print ('Authentication failed')
         exit (AuthenticationException)

