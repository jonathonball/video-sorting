from .directory import Directory
from .file import File
from .cache import IndexCache
import os
import sys

class VideoIndex:

    def __init__(self, args, config):
        self.args = args
        self.config = config
        self.search_paths = []
        self.search_types = []
        self.cache = IndexCache(args.indexdir)

    def set_search_paths(self, paths):
        paths = [Directory(path) for path in paths]
        self.search_paths = paths

    def set_search_types(self, types):
        types = [str(type) for type in types]
        self.search_types = types

    def build_index(self):
        self.cache.read_existing_index()
        for search_path in self.search_paths:
            for file in self.gather_media_files(search_path):
                if not self.cache.has_key(file.md5):
                    if self.args.verbose:
                        print("Added " + str(file.path))
                    file.fetch_media_info()
                    if file.is_valid_media_file():
                        self.cache.set(file.md5, file.to_dict())
                    else:
                        print("Skipping " + str(file.path) + ", invalid file", file=sys.stderr)
                else:
                    if self.args.verbose:
                        print("Skipping " + str(file.path) + ", exists.")
        self.cache.update_index()

    def gather_media_files(self, search_path):
        search_path = str(search_path)
        for path, dirs, filenames in os.walk(search_path, followlinks=self.args.followlinks):
            for filename in filenames:
                file = File(path, filename)
                if file.has_media_suffix(self.args.add_suffix):
                    yield file
