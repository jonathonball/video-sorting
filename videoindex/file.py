import os
import pathlib
import hashlib
from pymediainfo import MediaInfo


class File:

    def __init__(self, dirpath, filename):
        self.set_path_info(dirpath, filename)
        self.set_filename_hash()

    def __str__(self):
        return self.path

    def has_media_suffix(self, file_types):
        return self.suffix in file_types

    def set_path_info(self, dirpath, filename):
        self.dirpath = dirpath
        self.filename = filename
        self.path = os.path.join(self.dirpath, self.filename)
        self.suffix = pathlib.Path(self.path).suffix[1:]

    def set_filename_hash(self):
        self.filename_hash = hashlib.md5()
        self.filename_hash.update(self.path.encode('utf-8'))
        self.md5 = self.filename_hash.hexdigest()

    def to_dict(self):
        return {
            "dirpath": self.dirpath,
            "filename": self.filename,
            "path": str(self.path),
            "suffix": self.suffix,
            "filename_hash": self.md5,
            "media_info": self.media_info
        }

    def fetch_media_info(self):
        media_info = MediaInfo.parse(str(self.path))
        self.media_info = media_info.to_data()
        tracks = self.media_info['tracks']
        self.media_info['tracks'] = {
          "general": self.get_tracks_by_type(tracks, 'General'),
          "video":   self.get_tracks_by_type(tracks, 'Video'),
          "audio":   self.get_tracks_by_type(tracks, 'Audio')
        }

    def get_tracks_by_type(self, tracks, type):
        return [track for track in tracks if track['track_type'] == type]
