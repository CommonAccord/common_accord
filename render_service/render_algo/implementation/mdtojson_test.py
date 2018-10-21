#!/usr/bin/python
import pytest
from mdtojson import *
import json

def get_map_easy_maps_test():
    """This function tests the get_map
    function in the mdtojson on the
    set of easy maps"""

    assert getMap("test/etm/Alice") == json.load(open("test/etm/Alice.json"))
    assert getMap("test/etm/Bob") == json.load(open("test/etm/Bob.json"))
    assert getMap("test/etm/Moby_Dick") == json.load(open("test/etm/Moby_Dick.json"))
    assert getMap("test/etm/Purchase_Agreement") == json.load(open("test/etm/Purchase_Agreement.json"))



def get_tests():
    """gets all the tests
    """
    return [get_map_easy_maps_test]


if __name__ == '__main__' :

    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'