import argparse
import json
from .directory import Directory
from .file import File

class VideoIndex:

    def __init__(self, indexdir):
        self.indexdir = Directory(indexdir)
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
        # for search_location in self.search_locations:
        #     print(search_location)

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
