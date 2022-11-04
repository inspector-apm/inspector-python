from src.inspector.models import HasContext, Transaction
from src.inspector.models.partials import HOST
from src.inspector.models.enums import ModelType
import json

class Error(HasContext):
    model = ''
    timestamp = 0
    host = None
    transaction = None
    class_name = None
    file = None
    line = None
    code = None
    stack = []
    handled = None

    def __init__(self, throwable, transaction: Transaction):
        HasContext.__init__(self)
        self.model = ModelType.ERROR.value
        self.timestamp = self.get_microtime()
        self.host = HOST()
        self.transaction = transaction

        """
        
        $this->class = get_class($throwable);
        $this->file = $throwable->getFile();
        $this->line = $throwable->getLine();
        $this->code = $throwable->getCode();

        $this->stack = $this->stackTraceToArray(
            $throwable->getTrace(),
            $throwable->getFile(),
            $throwable->getLine()
        );
        
        """

    def set_handled(self, value):
        self.handled = value
        return self

    def stack_trace_to_array(self, stack_trace, top_file=None, top_line=None):
        pass

    def stack_trace_args_to_array(self, trace):
        pass

    def get_code(self, file_path, line, lines_around=5):
        pass

    def get_json(self) -> str:
        json_str = HasContext.get_json()
        json_str = json_str.replace('class_name', 'class')
        # return json_str
        return json.loads(
            json.dumps(self, default=lambda o: getattr(o, '__dict__', str(o)))
        )