var express = require('express');
var app = express();
var bodyParser = require('body-parser')
const fs = require("fs");


app.get('/', function (req, res) {
  res.send('Hello World');
})

app.use(express.json());

app.get('/render1', function (req, res) {
  res.send("hello")
})

app.post('/render', function (req, res) {
  // Call python script
  // Use Osprey, import RAML file to validate params
  // Call python file on toRender, lwGraph
  console.log("test")
  const key = req.body.key
  const graph = req.body.graph

  const spawn = require("child_process").spawn;
  // Need to figure out structure of tree to translate it to json
  const pythonProcess = spawn('python', ["../render_algo/ingress.py",
    key, graph]);
  
  parsed = ""
  
  pythonProcess.stdout.on('data', (data) => {
    // in case it returns in multiple chunks bc buffer size
    parsed = parsed + data.toString()
    // data is a dictionary representing the rendered tree
    // render_tree: {text: String (the variable name or the literal), metadata: {},
    //   children: [render_tree]}
  })

  pythonProcess.on('exit', (code) => {
    console.log(parsed)
    res.json(JSON.parse(parsed))
  })
})

// start the app

var server = app.listen(8081, function () {
  var host = server.address().address
  var port = server.address().port
})