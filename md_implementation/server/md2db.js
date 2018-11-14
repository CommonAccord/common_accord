//  TODO: A script for filling up our database with our md files
mongoose = require('mongoose');

// Connect to the database

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {});


// Call the python script

const pythonProcess = spawn('python', ['TODO: INSERT SOMETHING HERE'])

// insert returned values to db
pythonProcess.stdout.on('data', (op) => {
  op = JSON.parse(op)
  var toInput = new ProseObject({
    name: op.name,
    // this is the sketchy part...
    edges: [],
    data: op.data,
    parent: op.parent
  })

})