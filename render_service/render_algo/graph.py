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


    def find(self, key):
        """
        Find the best possible match of the key that
        is being searched for in the graph.

        If there is a tie, return the one with the highest priority.
        Returns a list of tokens that represent the value of the found
        key in the graph.
        """
        pass

    def search(self, depref):
        """
        Search for the input key in this graph

        Returns an error message or the list of tokens
        """
        pass

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
