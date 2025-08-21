# models/directions.py

from enum import Enum

class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

    def turn_right(self):
        members = list(Direction)
        index = (members.index(self) + 1) % len(members)
        return members[index]

    def turn_left(self):
        members = list(Direction)
        index = (members.index(self) - 1) % len(members)
        return members[index]
    
    def __str__(self):
        return self.name