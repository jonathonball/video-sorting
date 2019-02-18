from .directory import Directory

class VideoIndex:

    def __init__(self, indexdir):
        self.indexdir = Directory(indexdir)
        print(self.indexdir)
