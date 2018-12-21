# common_accord

README

# data structures used

## The node data structure
A node contains "data" and "edges", and has the following schema:

{
    "data": {
        "key_1": ["literal_1", "variable_1"],
        "key_2": ["literal_2"],
        "key_3": ["literal_3", "variable_2", "literal_4" ]
    },
    "edges": [["prefix_1", "node_2"]]
}

The data entry is a dictionairy since all the keys are unique and have no priority, while the edges entry is an array with the first element being of the highest priority.

The data is evaluated first, before looking at the edges field to see if the referenced maps might contain the value of a variable to be expanded. 

## The tree data structure
A traditional document is considered a particular "view" in this graph of nodes.
The node.py's render method does a depth-first search through the graph to return this "view." It also considers the priority and string value associated with each edge.
The outputted document, or "view" is a tree, that looks like this:

    Tree = {text: The variable name that resides originally in bracket, or just
                    a plain text for a literal
            metadata: {path: [edge path to where found], names: [vertex path ... ]},
            children: A list of Trees}

Note: each leaf is a literal, which has no metadata or children fields.







AUTHORS

Geoffrey Hazard
Xiaoman "Jerry" Chu
Jake Martin

Based-off of the model developed by James Hazard @ Commonaccord.org