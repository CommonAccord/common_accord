"""
Token class:
alternatively, reject having these classes altogether and have them be part of Graph
"""

class Token(object):

    def __init__(self):
        pass

class Literal(token):

    def __init__(self):
        pass

class Variable(token):
    """
    Variables exist as their fully-prefixed selves. This allows
    for a string-matching approach in graph's find method.
    """

    def __init__(self):
        pass
