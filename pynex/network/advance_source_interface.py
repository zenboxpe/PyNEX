from abc import ABC, abstractmethod

from pynex.network.network import Network
from pynex.network.source_interface import SourceInterface


class AdvanceSourceInterface(ABC, SourceInterface):

    @abstractmethod
    def block_address(self, address: str, timeout: int) -> None: pass

    @abstractmethod
    def unblock_address(self, address) -> None: pass

    @abstractmethod
    def set_network(self, network: Network) -> None: pass

    @abstractmethod
    def send_raw_packet(self, address: str, port: int, payload: bytearray): pass