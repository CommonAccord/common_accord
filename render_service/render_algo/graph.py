"""
Core render algorithm wrapped in the class Graph
"""
import json
import RenderTree from render_tree

class Graph(object):
    """
    A Graph is a dictionary with a predefined order
    """
    # NOTE: This implementation requires python 3.6 or above because it assumes
    #       that dictionaries maintain the ordering of keys.

    def __init__(self, refs, nonrefs, id):
        """
        Not yet implemented
        Assuming that there's a list
        """
        # dict: key -> Graph
        self.refs = refs
        # dict: key -> List<Tokens>
        self.nonrefs = nonrefs
        # id used for dfs
        self.id = id


    def render(self, key):
        """
        Render the input key according to this graph

        Returns the result of rendering the input key
        """
        # TODO: In Progress
        s = []
        acc = RenderTree()
        # NOTE: Do we error handle for invalid key?
        s[0:0] = find(self, key) #adding stack returned by find onto s stack

        while s:
            t = s.pop(0)
            if type(t) is Literal:
                acc.add_leaf(t)
            elif type(t) is Variable:
                acc.add_subtree(t)
                # add the new list of tokens to the top of the stack
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
        # search for key in self
        # loop over children and search for key there
        # len key is the length of the prefixes + self
        for i in range(len(key)):
            depref = key[i:]
            v = search(self, sum(depref))
            if v is not None:
                return v
            else:
                continue
        return None # this should be a custom error message

    def search(self, target):
        g = self
        stack = []
        visited = []
.       stack.append({"prefixes" : [], "path" : [self.id], "node": g})
        # can code in regex later... I'm not convinced of performance bump
        while stack:
            s = stack.pop()
            if s is in visited:
                continue
            else:
                visited.append(s)
                # add prefixes to target to create final value to match
                prefixed = sum(s["prefixes"]) + target
                if prefixed is in self.nonrefs.keys():
                    # we found what we're looking for
                    return {"path": s["path"], 
                        "value": self.nonrefs[item]}
                # we need to continue searching
                # add keys in reverse so that the first one gets popped first
                for k in self.refs.keys()[::-1]:
                    child_to_push = {"prefixes": s["prefixes"].append(k),
                        "path": s["path"].append(self.refs[k].id),
                        "node": self.refs[k]}
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
        return _decorate_recursive(json.loads(jstr))

    #TODO: Rewrite
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
    '''
