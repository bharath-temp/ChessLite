class MoveStatus():
    """Class for pieces that track if they've moved.

    This class overrides the `_on_position_changed` hook method
    to update the moved status when the piece's position changes.

    Attributes:
        _moved (bool): Indicates whether the piece has moved.
    """

    _moved = False

    def __init__(self) -> None:
        """ Ensure all piece get their own tracked moved var
            initialize to False
        """
        self._moved = False

    @property
    def moved(self) -> bool:
        """Indicates whether the piece has moved.

        Returns:
            bool: True if the piece has moved, False otherwise.
        """
        return self._moved

    @moved.setter
    def moved(self, has_moved: bool) -> None:
        """Sets the moved status of the piece.

        Args:
            has_moved (bool): True if the piece has moved, False otherwise.
        """
        self._moved = has_moved
