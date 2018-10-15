#!/usr/bin/python
import json

def getMap(name):
    """Takes in a string that is the name of an .md file
    and returns a json string
    Takes in name of file without the .md extension
    """

    h = { "data":{}, "edges":{} }
    for line in open(name+".md"):
        line = line[0:line.find("\n")] # removing newline char
        if "=" in line and not line.endswith("="):
            keyval = line.split("=")
            k = keyval[0]
            v = keyval[1]

            if "[" and "]" in v: # add to edges
                v = v[v.find("[")+1:v.find("]")] # removing brackets
                h["edges"][k]=v
            else: #add to data
                if not k in h:
                    h["data"][k]=v

    return json.dumps(h)
"""
if __name__ == '__main__' :
    print "testing getMap..."
    print getMap("test/Easy_Test_maps/Alice")
    print "testing done"
"""
