from __future__ import annotations
from typing import Union, Any
import json
import time
from abc import abstractmethod

class HasContext:
    _context: Union[None, dict] = {}

    # Add contextual information.
    # param: label
    # type: str|int
    # param: data
    # type: Any
    # return: HasContext
    def add_context(self, label: Union[str, int], data: Any) -> HasContext:
        self._context[label] = data
        return self

    # Set contextual information.
    # param: context
    # type: dict
    # return: HasContext
    def set_context(self, context: dict) -> HasContext:
        self._context = context
        return self

    # Get contextual information.
    # param: label
    # type: None|str|int
    # return: Any
    def get_context(self, label: Union[None, str, int] = None) -> Any:
        if label:
            if label in self._context:
                return self._context[label]
            else:
                return None
        return self._context

    # Convert the object to json recursively
    # return: str
    @abstractmethod
    def get_json(self) -> str:
        print('DICT SELF HAS_CONTEXT: ', self.__dict__)
        return json.loads(
            json.dumps(self, default=lambda o: getattr(o, '__dict__', str(o)))
        )

    def get_microtime(self):
        time_value = float(time.time() / 1000)
        return (round(time_value, 4))
