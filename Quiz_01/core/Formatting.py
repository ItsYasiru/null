from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Callable, Iterable


def prompt(prompt: str, cls: Any, invalid_prompt: str = "Invalid input!", *, check: Callable = None) -> None:
    """Handles user input and clean prompts and returns clean input retaining it's type"""
    if not prompt.endswith(" "):
        prompt += " "

    while (value := None) is None:
        try:
            value = cls(input(prompt))
            if check:
                if not check(value):
                    raise ValueError
            return value
        except (ValueError, TypeError):
            print(invalid_prompt)
        except KeyboardInterrupt:
            raise KeyboardInterrupt


def multi_str_ljust(data: Iterable[str], *, offset: int = None, append: str = ""):
    """Left aligns given strings in an iterable to a given or calculated offset optionally appending a sub-string"""
    offset = offset or max([len(datem) for datem in data]) + 1

    return [datem.ljust(offset) + append for datem in data]


def snakecase_to_camelcase(data: str, *, sep: str = "") -> str:
    """Converts snakecase to camelcase example : convert_this >>> ConvertThis"""
    return data.replace("_", sep).title()
