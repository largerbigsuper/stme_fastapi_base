from enum import Enum

class IssueStatusEnum(int, Enum):
    PENDING = -1
    FAIL = 0
    SUCCESS = 1

