from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class Queue(list):
    """Basic implementation of a repetitive queue"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__current: int = 0

    def __enter__(self) -> None:
        self.reset_index()

    def __exit__(self, *args, **kwargs) -> None:
        self.reset_index()

    def next(self) -> Any:
        """Returns the next item"""
        value = self[self.__current]
        self.__current += 1
        return value

    def reset_index(self) -> None:
        self.__current = 0
