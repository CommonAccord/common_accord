"""
Core Redner Algorithm wrapped in the class Graph
"""
import json

class Graph(object):
    """
    A Graph is a dictionary with a predefined order
    """

    def __init__(self, refs, nonrefs):
        """
        Not yet implemented
        """
        self.refs = refs
        self.nonrefs = nonrefs


    def render(self, key):
        """
        Render the input key according to this graph

        Returns the result of rendering the input key
        """

    def find(self, key):
        """
        Find the input key in this graph

        Returns a list of tokens represented by the given key
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
