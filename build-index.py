#!/usr/bin/env python3

import configparser
import os
import pathlib

this_script_fullpath = os.path.realpath(__file__)
this_script_dir = os.path.dirname(this_script_fullpath)

config = configparser.ConfigParser()
config['DEFAULT'] = {
  'follow_links': False,
  'search_dir': os.getcwd(),
  'index_dir': os.getcwd()
}

config.read(this_script_dir + '/options.ini')
follow_links = config.getboolean('File System', 'follow_links')
file_types = config.get('File System', 'file types').split(',')
search_dir = config.get('File System', 'search_dir')

for dirpath, dirnames, filenames in os.walk(search_dir, followlinks=follow_links):
    for file in filenames:
        file_full_path = os.path.join(dirpath, file)
        suffix = pathlib.Path(file_full_path).suffix[1:]
        if suffix in file_types:
            print(file_full_path)
