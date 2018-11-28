from node import Node
import json
import sys

def main(argv):
    root_node = Node.parse(" ".join(argv[1:]))
    tree = root_node.render(argv[0])
    print(json.dumps(tree))

if __name__ == "__main__":
    main(sys.argv[1:])
