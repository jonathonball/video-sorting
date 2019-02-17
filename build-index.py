#!/usr/bin/env python3

import configparser
import os
import pathlib
import argparse
import sys
from videodir import VideoDir

this_script_fullpath = os.path.realpath(__file__)
this_script_dir = os.path.dirname(this_script_fullpath)

config = configparser.ConfigParser()
config['DEFAULT'] = {
  'followlinks': False,
  'searchdir': os.getcwd(),
  'indexdir': os.getcwd()
}
config.read(this_script_dir + '/options.ini')

file_types = config.get('File System', 'file types').split(',')

parser = argparse.ArgumentParser(prog='build-index', description="Builds an index of media metadata for a given directory")
parser.add_argument('searchdir',
                    nargs   = '?',
                    default = config.get('File System', 'searchdir'),
                    type    = VideoDir,
                    help    = "Directory to search for media")
parser.add_argument('-l', '--followlinks',
                    default = config.getboolean('File System', 'followlinks'),
                    action  = "store_true",
                    help    = "Follow symbolic links")
parser.add_argument('-i', '--indexdir',
                    default = config.get('File System', 'indexdir'),
                    type    = VideoDir,
                    help    = "Directory to store media info index")
args = parser.parse_args()
#print(args, file=sys.stderr)

#
# for dirpath, dirnames, filenames in os.walk(search_dir, followlinks=follow_links):
#     for file in filenames:
#         file_full_path = os.path.join(dirpath, file)
#         suffix = pathlib.Path(file_full_path).suffix[1:]
#         if suffix in file_types:
#             print(file_full_path)
#
# print("follow_links: " + ("True" if follow_links else "False"))
# print("search_dir:   " + search_dir)
