#!/usr/bin/env python3

import configparser
import os
import pathlib
import argparse
import sys
from videodir import VideoDir
import pprint

pp = pprint.PrettyPrinter(indent=4)
this_script_fullpath = os.path.realpath(__file__)
this_script_dir = os.path.dirname(this_script_fullpath)

config = configparser.ConfigParser()
config['DEFAULT'] = {
  'followlinks': False,
  'searchdir': os.getcwd(),
  'indexdir': os.getcwd()
}
config.read(this_script_dir + '/options.ini')

parser = argparse.ArgumentParser(prog='build-index', description="Builds an index of media metadata for a given directory")
parser.add_argument('searchdir',
                    nargs   = '?',
                    default = config.get('File System', 'searchdir'),
                    help    = "Directory to search for media")
parser.add_argument('-l', '--followlinks',
                    default = config.getboolean('File System', 'followlinks'),
                    action  = "store_true",
                    help    = "Follow symbolic links")
parser.add_argument('-i', '--indexdir',
                    default = config.get('File System', 'indexdir'),
                    help    = "Directory to store media info index")
parser.add_argument('--add-suffix',
                    nargs   = '?',
                    default = config.get('File System', 'file types').split(','),
                    action  = 'append',
                    help    = "Comma separated list of valid file extensions")
args = parser.parse_args()
pp.pprint(args)
