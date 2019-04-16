from enum import Enum
class LogLevel(Enum):
    NONE = None
    EMERGENCY = None
    ALERT = None
    CRITICAL = None
    ERROR = None
    WARNING = None
    NOTICE = None
    INFO = None
    DEBUG = None

    DEFAULT_LEVEL = NONE

print(LogLevel['DEFAULT_LEVEL'])