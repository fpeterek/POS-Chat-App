import socket
from typing import Tuple


class Writer:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    @property
    def server(self) -> Tuple[str, int]:
        return self.host, self.port

    def _run(self):
        while True:
            line = input('> ')[0:256]

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.server)
                sock.sendall(bytes(line, encoding='utf-8'))

    def run(self):
        try:
            self._run()
        except:
            raise KeyboardInterrupt()


if __name__ == '__main__':
    writer = Writer('pcfeib425t', 8000)
    writer.run()
