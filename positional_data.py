from enum import Enum


class FieldGroup:
    OF = 'OF'
    IF = 'IF'
    BE = 'bench'


class Position:
    def __init__(self, title, number, field_group, shorthand):
        self.title = title
        self.number = number
        self.field_group = field_group
        self.shorthand = shorthand


class StandardPosition(Enum):
    _P = Position("pitcher", 1, FieldGroup.IF, "P")
    _C = Position("catcher", 2, FieldGroup.OF, "C")
    _1B = Position("first base", 3, FieldGroup.IF, "1B")
    _2B = Position("second base", 4, FieldGroup.IF, "2B")
    _SS = Position("short stop", 6, FieldGroup.IF, "SS")
    _3B = Position("third base", 5, FieldGroup.IF, "3B")
    _LF = Position("left field", 7, FieldGroup.OF, "LF")
    _LC = Position("left center", 8, FieldGroup.OF, "LC")
    _RC = Position("right center", 9, FieldGroup.OF, "RC")
    _RF = Position("right field", 10, FieldGroup.OF, "RF")
