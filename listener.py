import socket
import datetime


class Listener:

    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', port))
        self.last = ('127.0.0.1', datetime.datetime.fromtimestamp(0), '')

    def run(self):
        while True:
            data = self.sock.recv(9+255)

            # IP address
            ip = '.'.join([str(byte) for byte in data[0:4]])

            # Time and date
            time = int.from_bytes(data[4:8], byteorder='big', signed=False)
            date = datetime.datetime.fromtimestamp(time)

            # Message
            size = int(data[8])
            data = data[9:9+size].decode('utf-8', errors='replace')

            # Perform deduplication of messages
            if (ip, date, data) == self.last:
                continue

            print(f'[{ip} - {date}]: {data}')

            self.last = (ip, date, data)


if __name__ == '__main__':
    listener = Listener(8010)
    listener.run()
