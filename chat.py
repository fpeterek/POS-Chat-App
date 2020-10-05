import time
import sys
from threading import Thread

from listener import Listener
from writer import Writer


if __name__ == '__main__':
    listener = Listener(8010)
    writer = Writer('pcfeib425t', 8000)

    listen_thread = Thread(target=lambda: listener.run())
    writer_thread = Thread(target=lambda: writer.run())

    listen_thread.start()
    writer_thread.start()

    while True:
        try:
            time.sleep(60 * 60)
        except:
            break

    print('Shutting down...')
    sys.exit(0)
