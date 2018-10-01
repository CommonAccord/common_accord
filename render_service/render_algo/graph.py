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
        root = {'subtrees': [], 'where': []}

        stack = self.find(key)
        while stack:
            token = stack.pop()
            if type(token) is Literal:
                root['subtrees'].append({'subtrees': [], 'where'})

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
