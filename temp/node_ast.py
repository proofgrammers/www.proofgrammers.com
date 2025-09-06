import ast

class VisitNode:
    def __init__(self, source_path):
        self.code = None
        self.tree = None
        self.source_path = source_path
