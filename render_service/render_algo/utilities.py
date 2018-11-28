import re
import json
import sys
from node import Node

# Returns: Render tree as json string
def simple_render(graph, key):
    return json.dumps(Node.parse(graph).render(key))

def simple_simple(graph, key):
    return json.dumps(Node.flatten(Node.parse(graph).render(key)))

def render(graph, *keys):
    root = Node.parse(graph)
    for key in keys:
        yield json.dumps(root.render(key))

# This is md to json NOT FOR DATABASE
def md2json(name, directory):
    """
    md2json with fewer function calls, which means better performance ??
    """
    graph = dict()
    jdict = {"root": name, "graph": graph}
    unfinished = [name]
    while unfinished:
        current = unfinished.pop()
        if current not in graph:
            graph[current] = {"data": {}, "edges": []}
            with open(directory + "/" + current + ".md") as f:
                for line in f:
                    line = line.rstrip("\n")
                    for i, c in enumerate(line):
                        if "=" == c:
                            k = line[:i]
                            v = line[i+1:]
                            if v and v[0] == "[" and v[-1] == "]":
                                graph[current]["edges"].append([k, v[1:-1]])
                            else:
                                graph[current]["data"].setdefault(k, re.compile("[\\{\\}]").split(v))
                            break
            for edge, neighbor in graph[current]["edges"]:
                unfinished.append(neighbor)
    return json.dumps(jdict)

def mainOld():
    if len(sys.argv) < 3:
        print("Usage: python3 render.py <root name> <directory> [keys...]")
    rname = sys.argv[1]
    directory = sys.argv[2]
    keys = sys.argv[3:]
    root_node = Node.parse(md2json(rname, directory))

    for key in keys:

        pp = pprint.PrettyPrinter(indent=4) #prints data structures nicely
        pp.pprint(root_node.render(key))

def mainOld2():
    if len(sys.argv) < 3:
        print("Usage: python3 render.py <root name> <directory> [keys...]")
    rname = sys.argv[1]
    directory = sys.argv[2]
    keys = sys.argv[3:]
    root_node = Node.parse(md2json(rname, directory))
    for key in keys:
        with open(directory + "/" + key + ".html", "w") as f:
            f.write(Node.flatten(root_node.render(key)))

def main(argv):
    print(md2json(argv[0], argv[1]))

if __name__ == "__main__":
    main(sys.argv[1:])
