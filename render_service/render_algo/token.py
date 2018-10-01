"""
Token class:
alternatively, reject having these classes altogether and have them be part of Graph
"""

import json

class Token(object):

    def __init__(self, tokens):
        self.tokens = tokens

    @staticmethod
    def parse(jstr):
        """
        Parses the input json string
        jstr: A json string

        Returns the Graph representation of it
        """
        acc = []
        loaded = json.loads(jstr)
        for t in loaded:
            if t["type"] == "literal":
                acc.append(Literal(t["value"]))
            else:
                acc.append(Variable(t["value"]))

class Literal(token):

    def __init__(self, val):
        self.val = val

class Variable(token):
    """
    Variables exist as their fully-prefixed selves. This allows
    for a string-matching approach in graph's find method.
    """

<<<<<<< HEAD
    def __init__(self):
        pass

class notFound(token):
    """
    The graph's find method will instantiate keys that are not found
    as a notFound object
    """
    def __init__(self, key):
        self.key = key
=======
    def __init__(self, val):
        self.val = val
>>>>>>> 039bb431253bb85131d746ccc45b5209b5c14c08
