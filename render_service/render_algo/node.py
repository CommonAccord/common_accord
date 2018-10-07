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
    name: name of document
    """
    # NOTE: This implementation requires python 3.6 or above because it assumes
    #       that dictionaries maintain the ordering of keys.

    def __init__(self, refs, nonrefs, name):
        """
        Subgraphs is an object with contains a list key, graph pairs
        dictionary is the direct keys
        """
        # list of string, node pairs
        self.edges = refs
        # dict: string -> List<Tokens>
        self.data = nonrefs
        # name used for distinguishing edges with the same names
        self.name = name


    def render(self, key):
        """
        Render the input key according to this graph
        Creates a tree where each node has:
        Returns the result of rendering the input key
        """
        root = dict()
        unfinished = [([], key, root)]
        while unfinished:
            prefixes, var, tree = unfinished.pop()
            tokens, metadata = self.find(prefixes, var)
            tree["metadata"] = metadata
            parts = tree.setdefault("parts", [])
            for token in reversed(tokens):
                if isinstance(token, int): # Literal
                    parts.append(token)
                elif isinstance(token, str): # Variable
                    subtree = dict()
                    parts.insert(0, subtree)
                    unfinished.append((metadata["path"], token, subtree))
                else: # If correctly implemented, this should never happen
                    raise ValueError
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
        length, indirect, direct = Node._tabulate(filter(len, prefixes), var)
        visited = {self: set(0)}
        stack = [(self, 0, [], [])]
        standard = -1
        best = [], "Error: not found"
        while stack:
            node, level, path, names = stack.pop()
            for i in range(length, max(level - 1, standard), -1):
                tokens = node.data.get(direct[level][i], None)
                if tokens:
                    best = tokens, {"path": path, "names": names}
                    standard = i
                    break
            # The following shortcut could come up for a perfect match
            # And it is important because this gurantees faster runtime than the
            # naive approach even when there is a perfect match
            if standard == length:
                break
            node._expand(level, length, indirect[level], visited, stack, path, names)
        return best


    @staticmethod
    def _tabulate(prefixes, var):
        """
        This static helper basically construct tables for efficient string slicing

        The end result guarantees that when we do 'indirect[i][j]', where i <= j,
        we are getting '"".join(prefixes[i:j])' but in constant time

        Likewise 'direct[i][j] == "".join(prefixes[i:j]) + var'
        """
        length = len(prefixes)
        indirect = []
        direct = []
        for i in range(length):
            sentinel_i = {i: ""}
            sentinel_d = {i: var}
            acc = ""
            for j in range(i, length):
                acc += prefixes[j]
                sentinel_i[j+1] = acc
                sentinel_d[j+1] = acc + var
            indirect.append(sentinel_i)
            direct.append(sentinel_d)
        return length, indirect, direct


    def _expand(self, level, length, pref_table, visited, stack, path, names):
        """
        When this helper function is called, we look at all the edges the 'self'
        node is connected to and filter the ones that are both matching the path
        and unvisited and the corresponding level.
        """
        # Go through the edges in reversed priority to guarantee that the ones
        # with higher priority gets pushed onto the stack later
        for edge, neighbor in reversed(self.edges):
            name_len = len(edge)
            low, high = level, length
            # This while loop helps find the possible match in log(n) time
            # because the prefix table is sorted. Theoretically, this is the
            # best we can do without hashing, which is space inefficient and
            # hashing isn't actually free (takes more time when string is longer)
            #
            # We're using this binary search algorithm because it is reasonably
            # fast and space efficient. In reality however, this is really fast
            # anyway that we could've done it without any optimization whatsoever,
            # because paths are most likely really short anyway.
            while low < high:
                mid = (low + high) // 2
                if name_len > len(pref_table[mid]):
                    low = mid + 1
                else:
                    high = mid
            # After the loop, we must have low == high. And because we're never
            # excluding the possibly matching string from the low-high inclusive
            # bounds, if a match exists, it must be right here:
            if pref_table[low] == edge:
                # Check if the neighbor node has been visited at this level
                if low not in visited.setdefault(neighbor, set()):
                    # Make sure it is mark visited for future encounters
                    visited[neighbor].add(low)
                    # Mark it on the stack so we can deal with it later
                    stack.append((neighbor, low, path + [edge], names + [neighbor.name]))


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
