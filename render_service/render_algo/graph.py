"""
Core render algorithm wrapped in the class Graph
"""

class Graph(object):
    """
    A Graph is a dictionary with a predefined order
    """

    def __init__(self):
        """
        Not yet implemented
        Assuming that there's a list
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
        Find the best possible match in the graph for the key that
        is being searched for.

        If there is a tie, return the one with the highest priority.
        Returns a list of tokens that represent the given key
        """



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
