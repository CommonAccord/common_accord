"""
Core render algorithm wrapped in the class Graph
"""
import json

class Graph(object):
    """
    A Graph is a dictionary with a predefined order
    """

    def __init__(self, refs, nonrefs):
        """
        Not yet implemented
        Assuming that there's a list
        """
        self.refs = refs
        self.nonrefs = nonrefs


    def render(self, key):
        """
        Render the input key according to this graph

        Returns the result of rendering the input key
        """
        s = []
        acc = []

        s[0:0] = find(self,key) #adding stack returned by find onto s stack

        while s:
            t = s.pop(0)
            if type(t) is Literal:
                acc.append(t)
            elif type(t) is Variable:
                s[0:0] = find(self, key)

        return acc


    def find(self, key):
        """
        Finds the right value for the inputed key in 2 steps:
        1: Using regex to find the best possible string match of the key in the
        entire graph (taking into account prefixes of course).

        2: If there is a tie, chooses the value of the key with highest
        priority.

        Returns the value of the found key as a list of tokens.
        """

    @staticmethod
    def parse(jstr):
        """
        Parses the input json string
        jstr: A json string

        Returns the Graph representation of it
        """
        return _decorate_recursive(json.loads(jstr))

    @staticmethod
    def _decorate_recursive(dictionary):
        refs = {}
        nonrefs = {}
        priority = 0
        for key in dictionary:
            value = dictionary[key]
            if isinstance(value, dict):
                refs[key] = (priority, _decorate_recursive(value))
                priority += 1
            else:
                nonrefs[key] = value
        return Graph(refs, nonrefs)
