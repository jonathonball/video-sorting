import os
import pathlib
import argparse

class VideoDir:

    def __init__(self, path):
        self.check_path_exists(path)
        self.path = path

    def __str__(self):
        return self.path

    def check_path_exists(self, path):
        if (not os.path.isdir(path)):
            msg = "%s is not a valid path" % path
            raise argparse.ArgumentTypeError(msg)

    def to_string(self):
        return str(self)

# for dirpath, dirnames, filenames in os.walk(search_dir, followlinks=follow_links):
#     for file in filenames:
#         file_full_path = os.path.join(dirpath, file)
#         suffix = pathlib.Path(file_full_path).suffix[1:]
#         if suffix in file_types:
#             print(file_full_path)
#
