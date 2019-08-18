from enum import Enum


class Response:
    class Statuses(Enum):
        OK = 'ok'
        FAIL = 'fail'
        ERROR = 'error'

    def __init__(self, status, message=None):
        self.status = status
        self.message = message

    @classmethod
    def ok(cls, message=None):
        return cls(cls.Statuses.OK.value, message=message)

    @classmethod
    def fail(cls, message=None):
        return cls(cls.Statuses.FAIL.value, message=message)

    @classmethod
    def error(cls, message=None):
        return cls(cls.Statuses.ERROR.value, message=message)
