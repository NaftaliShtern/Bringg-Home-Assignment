from enum import Enum

class StatusCode(Enum):
    GenFound = 0
    GenNotFromSupportedTemplate = 1
    GenNotFound = 2
