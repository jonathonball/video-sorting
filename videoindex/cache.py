from .directory import Directory
import json


class IndexCache:

    def __init__(self, indexdir):
        self.indexdir = Directory(indexdir)
        self.index_file = str(self.indexdir) + '/.videoindex.json'
        self.index = {
            "files": {},
            "stats": {
                "resolution": {},
                "length": {},
                "bitrate": {},
                "codec": {}
            }
        }

    def has_key(self, key):
        return key in self.index['files']

    def get(self, key):
        if self.has_key(key):
            return self.index['files'][key]
        return None

    def set(self, key, value):
        self.index['files'][key] = value

    def get_stats(self):
        return self.index.stats

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
