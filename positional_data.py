from enum import Enum


class FieldGroup:
    OF = 'outfield'
    IF = 'infield'


class Position:
    def __init__(self, title, number, field_group):
        self.title = title
        self.number = number
        self.field_group = field_group


class StandardPosition(Enum):
    _P = Position("pitcher", 1, FieldGroup.IF)
    _C = Position("catcher", 2, FieldGroup.IF)
    _1B = Position("first base", 3, FieldGroup.IF)
    _2B = Position("second base", 4, FieldGroup.IF)
    _SS = Position("short stop", 6, FieldGroup.IF)
    _3B = Position("third base", 5, FieldGroup.IF)
    _LF = Position("left field", 7, FieldGroup.OF)
    _LC = Position("left center", 8, FieldGroup.OF)
    _RC = Position("right center", 9, FieldGroup.OF)
    _RF = Position("right field", 10, FieldGroup.OF)
