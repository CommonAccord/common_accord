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
        # list of string, node tuples
        self.edges = refs
        # dict: string -> List<Tokens>
        self.data = nonrefs
        # name used for distinguishing edges with the same names
        self.name = name


    def render(self, key):
        """
        Render the input key according to this graph

        Returns a tree with metadata
        """
        root = dict()
        unfinished = [([], key, root)]
        while unfinished:
            prefixes, var, tree = unfinished.pop()
            tokens, metadata = self.find(prefixes, var)
            tree["metadata"] = metadata
            parts = tree.setdefault("parts", [])
            for i, token in enumerate(reversed(tokens)):
                if i % 2 == 0: # Literal
                    parts.append(token)
                else: # Variable
                    subtree = dict()
                    parts.append(subtree)
                    unfinished.append((metadata["path"], token, subtree))
        # When everything is done, return the root
        return root


    def find(self, prefixes, var):
        """
        Given the prefixes and the variable, find the list of tokens associated
        with it.

        Returns a List<Token> - metadata pair, where metadata is a dictionary
        """
        fulls = [""]
        for prefix in prefixes:
            if prefix:
                fulls.append(fulls[-1] + prefix)
        fulls = [full + var for full in fulls]
        number_of_levels = len(fulls)
        possible_levels = range(number_of_levels-1, -1, -1)
        visited = {self: {0: set(possible_levels)}}
        stack = [(self, 0, possible_levels, [], [])]
        standard = -1
        best = ["<???>"], "Error: not found"
        while stack:
            node, mlen, possible_levels, path, names = stack.pop()
            still_possible = [l for l in possible_levels if l > standard]
            for level in still_possible:
                tokens = node.data.get(fulls[level][mlen:], None)
                if tokens:
                    best = tokens, {"path": path, "names": names}
                    standard = level
                    break
            # The following shortcut could come up for a perfect match
            # And it is important because this gurantees faster runtime than the
            # naive approach even when there is a perfect match
            if standard == number_of_levels:
                break
            if still_possible:
                node._expand(mlen, fulls, still_possible, visited, stack, path, names)
        return best

    """
    @staticmethod
    def _tabulate(prefixes, var):
        length = len(prefixes)
        indirect = []
        direct = []
        for i in range(length+1):
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
    """


    def _expand(self, mlen, fulls, possible_levels, visited, stack, path, names):
        """
        When this helper function is called, we look at all the edges the 'self'
        node is connected to and filter the ones that are both matching the path
        and unvisited and the corresponding level.
        """
        # Go through the edges in reversed priority to guarantee that the ones
        # with higher priority gets pushed onto the stack later
        for edge, neighbor in reversed(self.edges):
            new_possibilities = []
            tlen = len(edge) + mlen
            for level in possible_levels:
                if tlen > len(fulls[level]):
                    break
                if edge == fulls[level][mlen:tlen]:
                    # Check if the neighbor node has been visited at this mlen with given level
                    if level not in visited.setdefault(neighbor, dict()).setdefault(tlen, set()):
                        # Make sure it is mark visited for future encounters
                        visited[neighbor][tlen].add(level)
                        # Mark it on the stack so we can deal with it later
                        new_possibilities.append(level)
            if new_possibilities:
                stack.append((neighbor, tlen, new_possibilities, path + [edge], names + [neighbor.name]))

    # TODO: short-circuit comparison?
    def deep_equals(self, other_node):
        '''
        Compares nodes for equality at all levels (not just name). Used for testing.
        '''
        name_equals = other_node.name == self.name
        data_equals = self.data == other_node.data
        refs_equals = True

        # enforces ordering as well as equality
        for e1, e2 in zip(self.edges, other_node.edges):
            refs_equals = refs_equals and e1[0] == e2[0]
            refs_equals = refs_equals and e1[1].deep_equals(e2[1])

        refs_equals = refs_equals and len(self.edges) == len(other_node.edges)
        data_equals = self.data == other_node.data

        return name_equals and data_equals and refs_equals


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


    @staticmethod
    def flatten(tree):
        result = ""
        stack = [tree]
        while stack:
            current = stack.pop()
            if isinstance(current, str):
                result += current
                continue
            for each in current["parts"]:
                stack.append(each)
        return result

    @staticmethod
    def _flatten_recurs(tree):
        if isinstance(tree, str):
            return tree
        else:
            return "".join(map(Node.flatten, reversed(tree["parts"])))


    @staticmethod
    def parse(jstr):
        """
        Parses the input json string
        jstr: A json string w/ schema:
            name: str,
            edges: [{key: , node: }, ...]
            data: [{key: , tokens: [str/int, str/int, ...]}]

        Returns the Graph representation of it
        jstr = json.loads(jstr)
        name = jstr["name"]
        refs = jstr["edges"]
        nonrefs_temp = jstr["data"]

        refs = []
        for ele in refs:
            key = ele["key"]
            node = parse(ele["node"])
            str_to_node.append((key, node))

        nonrefs = {}
        for ele in nonrefs_temp:
            nonrefs[ele["key"]] = ele["tokens"]

        return Node(refs, nonrefs, name)
        """
        jstr = json.loads(jstr)
        root = jstr["root"]
        graph = jstr["graph"]
        parsed = {}
        for name in graph:
            parsed[name] = Node([], graph[name]["data"], name)

        for name in graph:
            for edge in graph[name]["edges"]:
                parsed[name].edges.append((edge[0], parsed[edge[1]]))

        return parsed[root]


    @staticmethod
    def parse_new(jstr):
        jstr = json.loads(jstr)
        root = jstr["root"]
        graph = jstr["graph"]
        parsed = {}
        parsed["root"] = root
        for k in jstr["graph"]:
            data = {}
            for ele in graph[k]["data"]:
                data[ele["key"]] = ele["tokens"]
            parsed[k] = Node([], data, k)

        for k in jstr["graph"]:
            for e in graph[k]["edges"]:
                key = e[0]
                filename = e[1]
                parsed[k].edges.append((key, parsed[filename]))

        return parsed[root]

    # prints the whole graph, depth first, starting at self
    def deep_to_string(self, indent=""):
        print(indent + "BEGIN NODE")
        indent += "  "
        print(indent + "name: " + self.name)
        print(indent + "data: " + json.dumps(self.data))
        print(indent + "edges: ")
        for e in self.edges:
            print(indent + "key: " + e[0])
            print(indent + "value: ")
            e[1].deep_to_string(indent)
            print(indent[:-2] + "END NODE")
    
