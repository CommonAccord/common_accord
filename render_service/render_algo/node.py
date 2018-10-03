"""
Core render algorithm wrapped in the class Graph
"""
import json
# import RenderTree from render_tree

class Node(object):
    """
    Node is the data structure that represents a legal document.
    Its most notable fields are:

    edges: a list of references to other documents with string associations
    data: a dictionary of local key-List<Token> pairs
    name: name of document (also used for dfs)
    """
    # NOTE: This implementation requires python 3.6 or above because it assumes
    #       that dictionaries maintain the ordering of keys.

    def __init__(self, refs, nonrefs, name):
        """
        Not yet implemented
        Assuming that there's a list
        """
        # list of string
        self.edges = refs
        # dict: key -> List<Tokens>
        self.data = nonrefs
        # name used for dfs
        self.name = name


    def render(self, key):
        """
        Render the input key according to this graph

        Returns the result of rendering the input key
        """
        root = {}
        unfinished = [(key, root)]
        while unfinished:
            var, tree = unfinished.pop()
            tokens, metadata = self.find(var)
            tree["metadata"] = metadata
            parts = tree.setdefault("parts", [])
            accumulated = []
            for token in tokens:
                if isinstance(token, int): # Literal
                    parts.append(token)
                elif isinstance(token, str): # Variable
                    parts.append(dict())
                    accumulated.insert(0, (token, {}))
                else: # If correctly implemented, this should never happen
                    raise ValueError
            unfinished += accumulated
        # When everything is done, return the root
        return root


    def find(self, key):
        """
        Finds the right value for the inputed key in 2 steps:
        1: Using regex to find the best possible string match of the key in the
        entire graph (taking into account prefixes of course).

        2: If there is a tie, chooses the value of the key with highest
        priority.

        Returns the value of the found key as a list of tokens.
        """
        # search for key in self
        # loop over children and search for key there
        # len key is the length of the prefixes + self
        for i in range(len(key)):
            depref = key[i:]
            v = self.search("".join(depref))
            if v is not None:
                return v
            else:
                continue
        return None # this should be a custom error message



    def search(self, target):
        g = self
        stack = []
        visited = []
.       stack.append({"prefixes" : [], "path" : [self.name], "node": g})
        # can code in regex later... I'm not convinced of performance bump
        while stack:
            s = stack.pop()
            if s is in visited:
                continue
            else:
                visited.append(s)
                # add prefixes to target to create final value to match
                prefixed = "".join(s["prefixes"]) + target
                if prefixed is in self.data:
                    # we found what we're looking for
                    return {"path": s["path"], "value": self.data[item]}
                # we need to continue searching
                # add keys in reverse so that the first one gets popped first
                for k in self.edges.keys()[::-1]:
                    child_to_push = {"prefixes": s["prefixes"].append(k),
                        "path": s["path"].append(self.edges[k].name),
                        "node": self.edges[k]}
                    stack.append(child_to_push)

        # This should be an error message ("Item not found")
        return None

    #TODO: Rewrite parse to fit new structure
    @staticmethod
    def parse(jstr):
        """
        Parses the input json string
        jstr: A json string

        Returns the Graph representation of it
        """
