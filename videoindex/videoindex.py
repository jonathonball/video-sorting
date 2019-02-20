import argparse
import json
from .directory import Directory
from .file import File
import os

class VideoIndex:

    def __init__(self, args, config):
        self.args = args
        self.config = config
        self.indexdir = Directory(args.indexdir)
        self.index_file = str(self.indexdir) + '/.videoindex.json'
        self.search_locations = []
        self.search_types = []
        self.index = {
            "files": [],
            "stats": {
                "resolution": {},
                "length": {},
                "bitrate": {},
                "codec": {}
            }
        }

    def set_search_locations(self, paths):
        paths = [Directory(path) for path in paths]
        self.search_locations = paths

    def set_search_types(self, types):
        types = [str(type) for type in types]
        self.search_types = types

    def build_index(self):
        self.read_existing_index()
        for search_location in self.search_locations:
            for path, dirs, filenames in os.walk(str(search_location), followlinks=self.args.followlinks):
                 for filename in filenames:
                     file = File(path, filename)
                     if file.has_media_suffix(self.args.add_suffix):
                         print(file.filename_hash.hexdigest())

    def read_existing_index(self):
        try:
            index = self.read_index_file()
        except FileNotFoundError:
            index = self.create_index()
        self.index = index

    def read_index_file(self):
        with open(self.index_file, "r") as open_file:
            index = json.load(open_file)
        return index

    def create_index(self):
        with open(self.index_file, "w") as new_index:
            json.dump(self.index, new_index, indent=4)
        return self.read_index_file()

    def update_index(self):
        with open(self.index_file, "w") as index:
            json.dump(self.index, index, indent=4)
