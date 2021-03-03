class ParamsIncorrect(Exception):
    def __init__(self, message='The both params are missed or filled. Expecting only one params'):
        super().__init__(message)