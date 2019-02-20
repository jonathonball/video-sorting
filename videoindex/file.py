import os
import argparse
import pathlib
import hashlib

class File:

    def __init__(self, dirpath, filename):
        self.dirpath = dirpath
        self.filename = filename
        self.path = os.path.join(self.dirpath, self.filename)
        self.suffix = pathlib.Path(self.path).suffix[1:]
        self.filename_hash = hashlib.md5()
        self.filename_hash.update(self.path.encode('utf-8'))

    def __str__(self):
        return self.path

    def has_media_suffix(self, file_types):
        return self.suffix in file_types

