#!/usr/bin/env python3

import configparser
config = configparser.ConfigParser()
config.read('options.ini')

recurse_through_filesystem = config.getboolean('File System', 'recurse')

print(recurse_through_filesystem);
