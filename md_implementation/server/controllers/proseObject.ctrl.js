let mongoose = require('mongoose');
let ProseObjectModel = require('../models/proseObject')

/*
  GET /objects - route to retrieve all objects. They will be structured like a
    filesystem. This only returns a light version of the set of objects: enough
    to determine the tree structure and display filenames.
    Note: This should eventually be expanded to "return all documents for
    a given user".
*/

function getObjects(req, res) {
  let query = proseObjectModel.find({}, "name parents");
  query.exec((err, objects) => {
    if (err) res.send(err)
    res.json(objects)
  }
  );
}

/*
  GET /object:id - route to retrieve the ProseObject with the given id.
    Returns a whole metadata tree. This means we have to crawl the database
    to construct the entire tree, expanding each reference in edges.
    Transforms the graph represented in the database into a dictionary.
    Returns a dictionary with two values:
      root: This root node of the returned graph
      graph: A list of nodes, each a dictionary exactly corresponding to the
              ProseObjectSchema.
*/

function getObjectId(req, res) {
    // initialize the lwGraph
    lwGraph = {
      "root": req.body.id,
      "graph": []
    };
    // push each edge onto the stack
    stack = []
    seen = {}
    // As long as there are still nodes that link to nodes not yet in lwGraph.graph,
    //   continue looping.
    while (stack.length != 0) {
      cur = stack.pop()
      // if we've already stored the node, continue looping
      if (seen.includes(cur)) continue;
      
      seen[cur] = true;
      ProseObjectModel.find({id: cur}).exec((err, object) => {
        if (err) res.send(err);

        let parsedObject = {
          id: object.id,
          name: object.name,
          edges: object.edges,
          data: object.data,
          parent: object.parent
        };
        lwGraph.graph.push(parsedObject);
        // push all of the object's edges onto the stack
        for (i = 0; i < object.edges.length; i++) {
          stack.push(object.edges[i]["proseObjectId"])
        }
      });
    }

    // TODO: Add a call to renderService... not sure how to do this yet
    
    // This will change... should be returning the renderTree
    res.json(lwGraph);
}

/*
  PUT /object:id - route to write to the Prose Object with the given id.
  Expects a json request of the form
  {
    changesArray : [{"target" : key}, {"value" : valToChangeTo},...],
    toChange : "id"
  }
*/

function putObjectId(req, res) {
  changesArray = req.body.changes;
  update = {}
  for (i = 0; i < changesArray.length; i++) {
    update[changesArray[i]["target"]] = [changesArray[i]["value"]]
  }
  id = req.body.toChange
  ProseObjectModel.findOneAndUpdate({id : id}, update).exec((err, object) => {
    if (err) res.send(err);

    // write success!
    res.send(200);
  })
}

/*
  DELETE /object:id - route to delete the Prose Object with the given id.
    NOTE: This may make it such that we would want to add "linked_to_by" to our
    data model because we may want to say "if you delete this you will break
    file1, file2, ...".
*/

function deleteObjectId(req, res) {
  toDelete = req.body.toDelete;

  ProseObjectModel.findOneAndDelete({id : toDelete}).exec((err, object) => {
    if (err) res.send(err);

    // delete success!
    res.send(200);
  })
}