// server/models/Article.js
const mongoose = require('mongoose');

objectId = mongoose.Schema.Types.ObjectId;

let ProseObjectSchema = new mongoose.Schema({
  // Name of the document
  name: String,
  // Edges, an array of tuples [(key, proseObjectId), ...]
  edges: [{
    key: String,
    proseObjectId: objectId
  }],
  // Data, a json array of type [{key: , tokens: [str/int, str/int, ...]}]
  data: [{
    key: String, 
    tokens: [String]
  }],
  // the id of the parent to allow us to simulate a file system for UX
  parent: String
});

module.exports = mongoose.model("ProseObject", ProseObjectSchema);