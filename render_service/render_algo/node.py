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
        Subgraphs is an object with contains a list key, graph pairs
        dictionary is the direct keys
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
        Creates a tree where each node has:
        Returns the result of rendering the input key
        """
        root = {}
        unfinished = [([], key, root)]
        while unfinished:
            prefixes, var, tree = unfinished.pop()
            tokens, metadata = self.find(prefixes, var)
            # TODO: add error checking, i.e. what if not found
            tree["metadata"] = metadata
            parts = tree.setdefault("parts", [])
            accumulated = []
            for token in tokens:
                if isinstance(token, int): # Literal
                    parts.append(token)
                elif isinstance(token, str): # Variable
                    subtree = dict()
                    parts.append(subtree)
                    accumulated.insert(0, (metadata["path"], token, subtree))
                else: # If correctly implemented, this should never happen
                    raise ValueError
            unfinished += accumulated
        # When everything is done, return the root
        return root


    def find(self, prefixes, var):
        """
        Finds the right value for the inputed key in 2 steps:
        1: Using regex to find the best possible string match of the key in the
        entire graph (taking into account prefixes of course).

        2: If there is a tie, chooses the value of the key with highest
        priority.

        Returns Path represented as list of strings that leads there
        the value of the found key as a list of tokens, and where it
        was found.
        """
        # search for key in self
        # loop over children and search for key there
        # len key is the length of the prefixes + self
        ran = range(len(prefixes) + 1)
        cummulative = list(map(lambda i: prefixes[i:], ran))
        for each in cummulative:
            each.append(var)

        length
        visited = {self: set(0)}
        stack = [(self, 0)]
        best = None
        standard = length
        while stack:
            node, level = stack.pop()
            for i in range(level, standard):
                tokens = node.data.get(direct[level][i], None)
                if tokens:
                    best = tokens, {"path": pass}
                    standard = i
                    # TODO: smart break
                    break
            for name, sub_node in reversed(node.edges):
                for i in range(level, length):
                    if indirect[level][i] == name:
                        if i not in visited.setdefault(sub_node, set()):
                            visited[sub_node].add(i)
                            stack.append((sub_node, i))
        return best


        for i in ran:
            stack = [(i, self)]
            visited = set()
            while stack:
                level, node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    tokens = node.data.get(cummulative[level], None)
                    if tokens:
                        return tokens, {"path": cummulative[i:level]}
                    for pref, sub_node in reversed(node.edges):
                        if pref == compartments[level] && sub_node:
                            stack.append((i + 1, sub_node))


        return None, None # this should be a custom error message


    '''
    def search(self, target):
        g = self
        stack = []
        visited = []
        stack.append({"prefixes" : [], "path" : [self.name], "node": g})
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
    '''

    #TODO: Rewrite parse to fit new structure
    @staticmethod
    def parse(jstr):
        """
        Parses the input json string
        jstr: A json string

        Returns the Graph representation of it
        """
