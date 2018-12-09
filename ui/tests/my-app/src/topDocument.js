import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import LeaseAgg from './LeaseAgg'

/*
  This class represents a the highest level document that is being displayed.
  We seperate subDoc from topDocument because only the top document should
  hold state.
*/

class topDocument extends Component {
    /*
    Tree = {metadata: {path: [edge path to where found], names: [vertex path ... ]},
    children: A list of Trees
    text: The variable name that resides originally}
    */
  constructor(props) {
    super(props);
    this.state = {
      renderTree: props.renderTree,
      
    }
  }

  // This function is used to edit the renderTree. Passed to children as prop
  // to lift up edits to the top level Document.
  editFunc(event) {
    // Add edit logic
    // Also needs to know at what level the edit takes place
    rt = null
    this.setState({renderTree: rt})
  }

  render() {
    renderTree = this.props.renderTree
    // text version of renderTree
    renderText = null;
    return (

    );
  }
}

export default App;