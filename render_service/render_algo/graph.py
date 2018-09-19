"""
Core Redner Algorithm wrapped in the class Graph
"""

class Graph(object):
    """
    A Graph is a dictionary with a predefined order
    """

    def __init__(self):
        """
        Not yet implemented
        """
        pass

    def render(self, key):
        """
        Render the input key according to this graph

        Returns the result of rendering the input key
        """
        pass

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
    def parse(json):
        """
        Parses the input json string

        Returns the Graph representation of it
        """
        pass
