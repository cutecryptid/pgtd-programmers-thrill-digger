class IncorrectStateError(Exception):
    pass

class GameIsOverException(IncorrectStateError):
    pass

class UnfinishedGameException(IncorrectStateError):
    pass