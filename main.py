import logging
import signal

from app import App

app = App()


def signal_handler(_signum, _stack):
    # Ctrl + C 退出
    global app
    logging.info('程序退出')
    app.close()


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    app.print_time()
