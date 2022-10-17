from src.inspector.models import Performance
from src.inspector.models.enums import ModelType
from src.inspector.models.partials import HOST


class Segment(Performance):
    MODEL_NAME = ModelType.SEGMENT.value
    model = None
    type = None
    label = None
    host = None
    start = None
    transaction = None

    def __init__(self, transaction, type, label):
        Performance.__init__(self)
        self.model = self.MODEL_NAME
        self.type = type
        self.label = label
        self.transaction = transaction
        self.host = HOST()

    def start(self, timestamp=None) -> Performance:
        initial = self.get_microtime() if timestamp is None else timestamp
        self.start = round((initial - self.transaction.timestamp) * 1000, 4)
        print('initial: ', initial)
        print('self.start: ', self.start)
        # return Performance.start(timestamp)
        return self
