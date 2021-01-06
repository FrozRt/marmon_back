from fastapi import HTTPException


class SettingNotFound(Exception):
    pass


class APIException(HTTPException):  # base class
    message: str
    status: int


class NotFound(APIException):
    message = 'Not found!'
    status = 404

    def __init__(self, detail=message, status_code=status, *args, **kwargs):
        super(NotFound, self).__init__(detail=detail, status_code=status_code, *args, **kwargs)


class RecordAlreadyExists(APIException):
    message = 'Record already exists!'
    status = 400

    def __init__(self, detail=message, status_code=status, *args, **kwargs):
        super(RecordAlreadyExists, self).__init__(detail=detail, status_code=status_code, *args, **kwargs)