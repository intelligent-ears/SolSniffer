class BaseRule:
    def __init__(self, ast):
        self.ast = ast
        self.issues = []

    def run(self):
        raise NotImplementedError
