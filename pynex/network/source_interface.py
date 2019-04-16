from abc import ABC, abstractmethod

from pynex.network.protocol.data_packet import DataPacket
from pynex.player import Player


class SourceInterface(ABC):

    @abstractmethod
    def put_packet(self, player: Player, packet: DataPacket, need_ACK: bool, immediate: bool): pass

    @abstractmethod
    def get_network_latency(self, player: Player): pass

    @abstractmethod
    def close(self, player: Player, reason: str) -> None: pass

    @abstractmethod
    def set_name(self, name: str): pass

    @abstractmethod
    def process(self): pass

    @abstractmethod
    def shutdown(self): pass

    @abstractmethod
    def emergency_shutdown(self): pass
