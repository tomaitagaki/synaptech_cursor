"""
A View is an abstract representation of the training interface.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple, List


@dataclass(frozen=True)
class ViewSetup:
    """
    ViewSetup represents a certain initial layout of the interface,
    as described by the window width, height, locations and size of targets,
    and initial position of cursor.
    """
    window_shape: Tuple[int, int]   # (width, height)
    targets: List[Tuple[int, int]]  # list of (x, y) pairs
    target_shape: Tuple[int, int]   # (width, height)
    cursor_pos: Tuple[int, int]     # (x, y)
    cursor_radius: int              # radius


class View(ABC):
    @abstractmethod
    def initialize(self, setup: ViewSetup):
        """
        Perform any initialization that the view requires and set up
        the initial trial visualization according to `setup`
        """
        pass

    @abstractmethod
    def move(self, x: int, y: int):
        """
        Moves the cursor to the specified (x, y) position.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Sets the interface to a blank window.
        """
        pass

    @abstractmethod
    def restart(self):
        """
        Resets the interface to the initial visualization of the trial.
        """
        pass

    @abstractmethod
    def update(self) -> bool:
        """
        Updates the interface and returns True if the user has not closed the view,
        False otherwise.
        """
        pass
