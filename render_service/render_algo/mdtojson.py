#!/usr/bin/python
import json

    and returns a json string
    Takes in name of file without the .md extension
    """

    h = { "data":{}, "edges":{} }
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
                    h["data"][k]= parseValue(v)
                    
    return json.dumps(h)

def parseValue(v):
    """In: the value to be parsed
    Out: a list of alternating Literals and  Variables.
    A Literal will always be the first element in the list.
    """

    #splitting value @ curly braces
    l = re.compile("[\\{\\}]").split(v)
    return l

if __name__ == '__main__' :
    print "testing getMap..."
    print getMap("test/Easy_Test_maps/Alice")
