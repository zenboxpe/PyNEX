from abc import ABC, abstractmethod

from pyromine.utils.binary import Binary


class AcknowledgePacket(ABC):
    RECORD_TYPE_RANGE = 0
    RECORD_TYPE_SINGLE = 1

    packets = []

    @abstractmethod
    def encode_payload(self) -> None:
        payload = ''
        self.packets.sort()
        count = len(self.packets)
        records = 0

        if count > 0:
            pointer = 1
            start = self.packets[0]
            last = self.packets[0]

            while pointer < count:
                current = self.packets[pointer+1]
                diff = current - last
                if(diff == 1):
                    last = current
                elif diff > 1:
                    if start is last:
                        payload += chr(self.RECORD_TYPE_SINGLE)
                        payload += Binary.write_l_triad(start)
                        start = last = current
                    else:
                        payload += chr(self.RECORD_TYPE_RANGE)
                        payload += Binary.write_l_triad(start)
                        payload += Binary.write_l_triad(last)
                        start = last = current

                    records+=1

            if start is last:
                payload += chr(self.RECORD_TYPE_SINGLE)
                payload += Binary.write_l_triad(start)
            else:
                payload += chr(self.RECORD_TYPE_RANGE)
                payload += Binary.write_l_triad(start)
                payload += Binary.write_l_triad(last)

            records+=1
        self.put_short(records)
        self.buffer += payload

    def decode_payload(self) -> None:
        count = self.get_short()
        self.packets = []
        cnt = 0
        # TODO: not yet