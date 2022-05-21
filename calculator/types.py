from enum import Enum, auto

class Operations(Enum):
    """Describes the types of operations possible"""
    
    # Basic Arithmetic
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()

Value = str | int | float

ParsedArr = list[Operations | ]