from build.lib.pynex.server import Server
from pynex.network.advance_source_interface import AdvanceSourceInterface
from pynex.network.source_interface import SourceInterface


class Network:

    CHANNEL_NONE = 0
    CHANNEL_PRIORITY = 1
    CHANNEL_WORLD_CHUNKS = 2
    CHANNEL_MOVEMENT = 3
    CHANNEL_BLOCKS = 4
    CHANNEL_WORLD_EVENTS = 5
    CHANNEL_ENTITY_SPAWNING = 6
    CHANNEL_TEXT = 7
    CHANNEL_END = 31

    server: Server

    interfaces = SourceInterface
    advance_interfaces = AdvanceSourceInterface

    upload = 0
    download = 0

    name = ''
    sun_name = ''

    def __init__(self, server: Server):
        self.register_packets()
        self.server = server

    def add_statistics(self, upload, download):
        self.upload += upload
        self.download += download

    def get_upload(self):
        return self.upload

    def get_download(self):
        return self.download

    def reset_statistics(self):
        self.upload = 0
        self.download = 0

    def get_interfaces(self):
        return self.interfaces



if __name__ == "__main__":
    t = Network
    print(t.get_interfaces())

