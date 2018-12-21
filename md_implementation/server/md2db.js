//  TODO: A script for filling up our database with our md files
mongoose = require('mongoose');
ProseObject = require('./models/proseObject');

// Connect to the database

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {});


// Call the python script
todo = {}
const pythonProcess = spawn('python', ['TODO: INSERT SOMETHING HERE'])

// insert returned values to db
pythonProcess.stdout.on('data', (output) => {
  output = JSON.parse(op)
  const keys = todo.keys;
  for (i = 0; i < output.length; i++)  {
    op = output[i];
  
    for (j = 0; j < todo.keys.length; j++) {
      toFill = [];
      const cur = todo[key];

      for (k = 0; k < todo[key].length; k++) {
        ProseObject.find({
          name: todo[key][k].name
        }, (err, obj2fill) => {
          if (err) continue;

          toFill.push({
            index: todo[key][k].index,
            id: obj._id
          })
        })
      }

      for (k = 0; k < toFill.length; k++) {
        ProseObject.findAndUpdate({name: todo.keys.})
      }
    }
    var toInput = new ProseObject({
      name: op.name,
      // this is the sketchy part...
      edges: [],
      data: op.data,
      parent: op.parent
    })
    edges = [];
    for (j = 0; j < op.edges.length; j++) {
      // TODO: Double check that name is the unique thing
      ProseObject.find({name: op.edges[j].name}, (err, obj) => {
        if (err) {
          // we haven't seen this edge yet
          // note this fact that we need to place this in the db in todo
          todo[op.name].push({"name" : op.edges[j].name, "index" : j})
          // push a dummy value to maintain the ordering of edges
          edges.push({key: op.edges[j].key, proseObjectId: "NULL"})
        } else {
          // we have seen this object
          edges.push({key: op.edges[j].key, proseObjectId: obj._id})
        }
      }); 
    }
    toInput.edges = edges;
    toInput.save((err, toInput) => {if (err) console.err(err)});
  }
})