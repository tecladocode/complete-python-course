class RuntimeErrorWithCode(Exception):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


err = RuntimeErrorWithCode('An error happened.', 500)
