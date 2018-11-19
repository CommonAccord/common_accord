#!/usr/bin/python
import json
import re
import pprint

def m2j(name, directory):
    """
    In: A string for the name of the a root file and 
    another for the directory where it is found

    Out: 

    md2json with fewer function calls, which means better performance ??
    """
    graph = dict()
    stack = [name]

    while stack:
        current = stack.pop()
        if current not in graph:
            graph[current] = {"name": current, "edges": [], "data": {}}
            
            with open(directory + "/" + current + ".md") as f:
                for line in f:
                    line = line.rstrip("\n")

                    for i, c in enumerate(line): #splitting by equals sign
                        if "=" == c:
                            k = line[:i]
                            v = line[i+1:]
                            # line could be a reference to another file
                            if v and v[0] == "[" and v[-1] == "]": 
                                graph[current]["edges"].append({"prefix": k , "objectId": v[1:-1]})
                            else: # if not must be key, value pair so add to data
                                graph[current]["data"].setdefault(k, re.compile("[\\{\\}]").split(v))
                            break

            for edge in graph[current]["edges"]:
                stack.append(edge["objectId"])

    for name, node in graph.items():
        for edge in node["edges"]:
            print("searching for", edge["objectId"],"dict in graph")
            edge["objectId"] = id(graph[edge["objectId"]])
                
    print(json.dumps(graph))

def md2json(name, directory):
    """
    Takes a name of a md file (without postfix) and a directory and produce a
    json string representation of the light weight graph
    """
    graph = dict()
    jdict = {"root": name, "graph": graph}
    unfinished = [name]
    while unfinished:
        current = unfinished.pop()
        if current not in graph:
            graph[current] = getMap(directory + "/" + current + ".md")
            for edge, neighbor in graph[current]["edges"]:
                unfinished.append(neighbor)
    return json.dumps(jdict)


def getMap(full_path):
    """Takes in a string that is the name of an .md file
    and returns a json string
    Takes in name of file without the .md extension
    """

    h = { "data":{}, "edges":[] }
    with open(full_path) as f:
        for line in f:

            line = line.rstrip("\n") # removing newline char

            # separating keys and values
            for i, c in enumerate(line):
                if "=" != c:
                    continue
                k = line[:i]
                v = line[i+1:]

                if len(v) > 1 and v[0] == "[" and v[-1] == "]": # is an edge
                    v = v[1:-1] # remove brackets
                    # add to edges list
                    h["edges"].append([k,v])

                else: # is data
                    if not k in h:
                        # add to data dict
                        h["data"][k]= parseValue(v)
                break

    return h

def parseValue(v):
    """In: the value to be parsed
    Out: a list of alternating Literals and  Variables.
    Both the first and last element in the list will always be a
    Literal.
    """

    #splitting value @ curly braces
    l = re.compile("[\\{\\}]").split(v)
    return l

if __name__ == '__main__' :
    print(m2j("Purchase_Agreement", "test/etm"))
