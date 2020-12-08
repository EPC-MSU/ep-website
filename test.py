

class Server:
    def __init__(self):
        pass

    def is_success(self) -> bool:
        return False

    def set_settings(self, settings):
        pass


def set_host(host: str):
    ...
    server = Server()
    server.set_settings(3)

    while not server.is_success():
        yield False
    yield True


def timer_callback(host_state):
    if next(host_state):
        timer.stop()


def foo():
    host_state = set_host("172.0.0.1")
    timer.start()
