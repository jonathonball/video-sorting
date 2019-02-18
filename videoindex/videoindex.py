from .directory import Directory

class VideoIndex:

    def __init__(self, indexdir):
        self.indexdir = Directory(indexdir)
        self.search_locations = []
        self.search_types = []

    def set_search_locations(self, paths):
        paths = [Directory(path) for path in paths]
        self.search_locations = paths

    def set_search_types(self, types):
        types = [str(type) for type in types]
        self.search_types = types
