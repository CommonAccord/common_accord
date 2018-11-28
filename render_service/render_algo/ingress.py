from node import Node
import json
import sys

def main(argv):
    """
    Takes in the first argument the key
    the second argument is the json string

    What's returned is the rendered tree with the following structure

    Tree = {metadata: {path: [edge path to where found], names: [vertex path ... ]},
            children: A list of Trees
            text: The variable name that resides originally}
    """
    root_node = Node.parse(" ".join(argv[1:]))
    tree = root_node.render(argv[0])
    print(json.dumps(tree))

if __name__ == "__main__":
    main(sys.argv[1:])
