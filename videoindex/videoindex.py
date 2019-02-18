from .directory import Directory

class VideoIndex:

    def __init__(self, indexdir):
        self.indexdir = Directory(indexdir)
        self.search_locations = []

    def add_search_locations(self, paths):
        paths = [Directory(path) for path in paths]
        self.search_locations = paths
