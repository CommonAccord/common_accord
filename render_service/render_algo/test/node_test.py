import pytest
import sys
sys.path.insert(0, '..')
from node import Node

def test_deepEquals():
  test1 = Node([], ("hello", ["1", "2"]), "test1")
  test2 = Node([], ("hello", ["1", "2"]), "test1")
  test3 = Node([("test1", test1)], ("hello1", ["1", "2"]), "test2")
  test4 = Node([("test1", test1)], ("hello1", ["1", "2"]), "test2")
  assert test1.deep_equals(test2)
  assert test3.deep_equals(test4)


def test_parse():
  test1 = "{\"name\": \"test1\", \"edges\": [], \"data\": [{\"key\": \"hello\", \"tokens\": [1, 2, \"3\"]}]}"
  test1_node = Node([], {"hello": [1, 2, "3"]}, "test1")
  to_verify = Node.parse(test1)
  
  assert Node.parse(test1).deep_equals(test1_node)

def test_new_parse():
  test1 = "{ \
      \"root\": \"name\", \
     	\"graph\": { \
            \"name\": { \
                \"edges\": [], \
                \"data\": [{ \
                    \"key\": \"hello\", \
                				\"tokens\": [{ \
                          \"type\": \"literal\", \
                          \"value\": 1 \
                        }, { \
                            \"type\": \"literal\", \
                            \"value\": 2 \
                        }, { \
                            \"type\": \"literal\", \
                            \"value\": \"3\" \
                        }] \
                }] \
            } \
	  } \
  }"
  test2 = "{ \
      \"root\": \"name\", \
     	\"graph\": { \
            \"name\": { \
                \"edges\": [[\"key1\", \"name1\"]], \
                \"data\": [{ \
                    \"key\": \"hello\", \
                				\"tokens\": [{ \
                          \"type\": \"literal\", \
                          \"value\": 1 \
                        }, { \
                            \"type\": \"literal\", \
                            \"value\": 2 \
                        }, { \
                            \"type\": \"literal\", \
                            \"value\": \"3\" \
                        }] \
                }] \
              }, \
              \"name1\": { \
                \"edges\": [], \
                \"data\": [{ \
                    \"key\": \"hello\", \
                				\"tokens\": [{ \
                          \"type\": \"literal\", \
                          \"value\": 1 \
                        }, { \
                            \"type\": \"literal\", \
                            \"value\": 2 \
                        }, { \
                            \"type\": \"literal\", \
                            \"value\": \"3\" \
                        }] \
                }] \
              } \
            } \
	  }"
  test2_node2 = Node([], {"hello": [{"type": "literal", "value": 1}, {
      "type": "literal", "value": 2}, {"type": "literal", "value": "3"}]},
      "name1")
  test2_node = Node([("key1", test2_node2)], {"hello": [{"type": "literal", "value": 1}, {
                    "type": "literal", "value": 2}, {"type": "literal", "value": "3"}]},
                    "name")
  test1_node = Node([], {"hello": [{"type": "literal", "value": 1}, {
                    "type": "literal", "value": 2}, {"type": "literal", "value": "3"}]},
                    "name")
  print(Node.parse_new(test1).name)
  print(Node.parse_new(test1).edges)
  print(Node.parse_new(test1).data)
  print(test1_node.name)
  print(test1_node.edges)
  print(test1_node.data)
  assert Node.parse_new(test1).deep_equals(test1_node)
  assert Node.parse_new(test2).deep_equals(test2_node)

