#!/usr/bin/env python3

import copy
import delete
import create

vars['dailydir'] = time.strftime("%Y%m%d")
vars['namedir'] = "Sauvegardedu" + dailydir + ".tar"
vars['local_path'] = '/home/localuser/Saves'
vars['ip_address'] = "192.168.0.2"
vars['name'] = "distantuser"
vars['passw'] = "root"
vars['remote_path'] = '/home/distantuser/Saves'

create(vars)
ssh = connect(vars)
copy(ssh, vars)
delete(ssh, vars)
