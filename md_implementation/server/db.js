// for testing the database

var mongoose = require('mongoose');
var ProseObject = require('./models/proseObject.js')
mongoose.connect('mongodb://localhost/test');

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
  // we're connected!
  console.log("connected!")
});

var first = new ProseObject({
  name: 'test2', 
  edges:[], 
  data: [{key: "10", tokens: []}],
  parent: 'NULL'});

first.save(function (err, fluffy) {
  if (err) return console.error(err);
  console.log("save success!")

  ProseObject.find({
    name: 'test'
  }).exec(function (err, docs) {
    if (err) console.error(err);
    dataKey = docs[0]._id
    console.log(JSON.stringify(docs));

    // ProseObject.deleteMany({name: 'test'}).exec((err, res) => {});
  });
});