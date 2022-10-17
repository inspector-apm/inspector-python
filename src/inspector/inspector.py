from __future__ import annotations
from . import Configuration
from src.inspector.models.enums import TransportType
from src.inspector.models import Transaction, Segment
from src.inspector.models.enums import TransactionType, ModelType

# import http.client
# import multiprocessing
from src.inspector.transports import CurlTransport


class Inspector:
    # Agent configuration.
    # type: Configuration
    _configuration: Configuration = None

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
        self._configuration = configuration
        if configuration.get_transport() == TransportType.ASYNC:
            # self._transport = AsyncTransport(configuration)
            pass
        else:
            self._transport = CurlTransport(configuration)

    def __del__(self):
        self.flush()

    def set_transport(self, resolver):
        pass

    def start_transaction(self, name, type_str=TransactionType.PROCESS.value):
        self._transaction = Transaction(name, type_str)
        self._transaction.start()
        self.add_entries(self._transaction)
        return self._transaction

    # Get current transaction instance.
    # return null|Transaction
    def current_transaction(self):
        return self._transaction

    # Determine if an active transaction exists.
    # return: bool
    def has_transaction(self) -> bool:
        return True if self._transaction else False

    # Determine if the current cycle hasn't started its transaction yet.
    # return: bool
    def need_transaction(self) -> bool:
        return self.is_recording() and not self.has_transaction()

    # Determine if a new segment can be added.
    # return: bool
    def can_add_segments(self) -> bool:
        return self.is_recording() and self.has_transaction()

    # Check if the monitoring is enabled.
    # return: bool
    def is_recording(self) -> bool:
        return self._configuration.is_enabled()

    # Enable recording.
    # return: Inspector
    def start_recording(self) -> Inspector:
        self._configuration.set_enabled(True)
        return self

    # Disable recording.
    # return: Inspector
    def stop_recording(self) -> Inspector:
        self._configuration.set_enabled(False)
        return self

    def start_segment(self, type_str=TransactionType.PROCESS.value, label=None):
        segment = Segment(self._transaction, type_str, label)
        segment.start()
        self.add_entries(segment)
        return segment

    def add_segment(self, callback, type, label=None, throw=False):
        pass

    def report_exception(self, exception, handled=True):
        pass

    def add_entries(self, entries) -> Inspector:
        # entries = entries if type(entries) is 'dict' else [entries]
        self._transport.add_entry(entries)
        return self

    @staticmethod
    def before_flush(self, callback):
        pass

    def flush(self):
        if not self.is_recording() or not self.has_transaction():
            return

        if not self._transaction.is_ended():
            self._transaction.end()

        self._transport.flush()
        # del self._transaction
