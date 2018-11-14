import sys
from implementation.mdtojson import md2json
from render_algo.node import Node

import pprint

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 render.py <root name> <directory> [keys...]")
    rname = sys.argv[1]
    directory = sys.argv[2]
    keys = sys.argv[3:]
    root_node = Node.parse(md2json(rname, directory))

    for key in keys:

        pp = pprint.PrettyPrinter(indent=4) #prints data structures nicely
        pp.pprint(root_node.render(key))
