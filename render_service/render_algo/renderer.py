import json
import argparse
import sys

import Graph from graph
import Token from token

print('{metadata: bloop, render_tree: blorp}')
sys.stdout.flush()

parser = argparse.ArgumentParser(description="Renders a string from a graph")

parser.add_argument("to_render", help="The string to render, represented as" +
  "json. Format: [{type: literal / variable, value: a string}]")
parser.add_argument("graph", help="The graph to renderon, represented as json. " +
  "Format: [{refs: [tokens, in, order], nonrefs: [other graphs, in order]}]")

#TODO: Add error handling

# parse
to_render = Token.parse(parser.to_render)
lw_graph = Graph.parse(parser.graph)

rendered = lw_graph.render(to_render)