class IncorrectStateError(Exception):
    pass

class GameAlreadyStartedError(IncorrectStateError):
    pass

class GameIsOverError(IncorrectStateError):
    pass

class UnfinishedGameError(IncorrectStateError):
    pass