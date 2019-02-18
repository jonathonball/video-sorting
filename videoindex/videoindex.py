from .directory import Directory

class VideoIndex:

    def __init__(self, indexdir):
        self.indexdir = Directory(indexdir)
        self.search_locations = []

    def add_search_location(self, path):
        new_path = Directory(path)
        self.search_locations.append(new_path)
