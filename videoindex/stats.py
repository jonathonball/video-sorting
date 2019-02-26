from .stat import Stat


class Stats:

    def __init__(self):
        self.data = {}

    def to_dict(self):
        return self.data

    def update_stat(self, stat, value):
        if stat in self.data:
            self.data[stat].add(value)
        else:
            self.data[stat] = Stat(value)

# "stats": {
#     "resolution": {},
#     "length": {},
#     "bitrate": {},
#     "codec": {}
# }
