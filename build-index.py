#!/usr/bin/env python3

import configparser
import os

this_script_fullpath = os.path.realpath(__file__)
this_script_dir = os.path.dirname(this_script_fullpath)

config = configparser.ConfigParser()
config.read(this_script_dir + '/options.ini')
file_types = config.get('File System', 'file types').split(',')

#recurse_through_filesystem = config.getboolean('File System', 'recurse')
