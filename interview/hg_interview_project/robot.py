class Robot:
    def __init__(self, x=0, y=0) -> None:
        self.set_position(x, y)

    def set_position(self, x, y) -> None:
        """
        Set the current position of the robot

        Args:
            x (int): Sets the x coordinate
            y (int): Sets the y coordinate
        """
        self.x = x
        self.y = y

    def get_position(self):
        """
        Returns the current position of the Robot

        Returns:
            int x: x coordinate
            int y: y coordinate
        """
        return self.x, self.y

    def move(self, moveset):
        """
        This method moves the robot U,D,L,R

        Args:
            move (char): Movement character
        """
        if len(moveset) > 0:
            for move in moveset:
                if move == "U":
                    self.set_position(self.x, self.y + 1)
                elif move == "D":
                    self.set_position(self.x, self.y - 1)
                elif move == "L":
                    self.set_position(self.x - 1, self.y)
                elif move == "R":
                    self.set_position(self.x + 1, self.y)
                else:
                    raise ValueError(f"Invalid Move '{move}'")
