from . import Configuration


class Inspector:
    # Agent configuration.
    # type: Configuration
    _configuration = None

    # Transport strategy.
    # type:
    _transport = None

    # Current transaction.
    # type:
    _transaction = None

    # Runa callback before flushing data to the remote platform.
    # type:
    _beforeCallbacks = []

    def __init__(self, configuration: Configuration):
        if configuration.get_transport() == 'async':
            # self._transport = AsyncTransport(configuration)
            pass
        else:
            # self._transport = CurlTransport(configuration)
            pass

    def set_transport(self, resolver):
        pass

    def start_transaction(self, name):
        pass

    def currentTransaction(self):
        pass

    def has_transaction(self) -> bool:
        return False

    def need_transaction(self) -> bool:
        return False

    def can_add_segments(self) -> bool:
        return False

    def is_recording(self) -> bool:
        return False

    def start_recording(self):
        pass

    def stop_recording(self):
        pass

    def start_segment(self, type, label=None):
        pass

    def add_segment(self, callback, type, label=None, throw=False):
        pass

    def report_exception(self, exception, handled=True):
        pass

    def add_entries(self, entries):
        pass

    @staticmethod
    def before_flush(self, callback):
        pass

    def flush(self):
        pass
