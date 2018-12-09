# common_accord

README

## The tree data structure
A traditional document is considered a particular "view" in this graph of relationships.
The node.py's render methoddoes a depth-first search through the graph to return this "view." It also considers the priority and string value associated with each edge.
The outputted document, or "view" is a tree, that looks like this:

    Tree = {text: The variable name that resides originally in bracket, or just
                    a plain text for a literal
            metadata: {path: [edge path to where found], names: [vertex path ... ]},
            children: A list of Trees}

Note: each leaf is a literal, which has no metadata or children fields.

TODO: please remove the curly braces that sorround the text key of variables. Should have {text: "Purchase_Agreement ... } and not {text: {"Purchase_Agreement"} ...}






AUTHORS

Geoffrey Hazard
Xiaoman "Jerry" Chu
Jake Martin

Based-off of the model developed by James Hazard @ Commonaccord.org