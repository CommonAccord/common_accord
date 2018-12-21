var request = require('request')
const fs = require("fs");

var headersOpt = {
  "content-type": "application/json",
};


const data = fs.readFileSync("lw_graph.json", 'UTF-8')
const root_key = 'Model.Root'

request({
  method: 'POST',
  url: 'http://localhost:8081/render',
  body: {key: root_key, graph: data},
  headers: headersOpt,
  json: true
}, function(error, response, body) {
  console.log(body)
  console.log(JSON.stringify(body))
})