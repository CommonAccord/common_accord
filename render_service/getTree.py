import sys
from implementation.mdtojson import md2json
from render_algo.node import Node

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 render.py <root name> <directory> [keys...]")
    rname = sys.argv[1]
    directory = sys.argv[2]
    keys = sys.argv[3:]
    root_node = Node.parse(md2json(rname, directory))

    for key in keys:
        print(root_node.render(key))
