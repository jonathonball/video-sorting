import os
import argparse

class Directory:

    def __init__(self, path):
        self.check_path_exists(path)
        self.path = path

    def __str__(self):
        return self.path

    def check_path_exists(self, path):
        if (not os.path.isdir(path)):
            msg = "%s: invalid path or insufficient permissions" % path
            raise argparse.ArgumentTypeError(msg)
