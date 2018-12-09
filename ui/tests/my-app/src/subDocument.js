import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import LeaseAgg from './LeaseAgg'

/*
  This class represents a document that is nested within a larger document.
  We seperate subDoc from topDocument because only the top document should
  hold state.
*/
class SubDocument extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isExpanded: true,
      // editFunc is a callback that allows us to lift up edits to the render tree
      // in the top level document
      editFunc: this.props.editFunc
    }
  }

  render() {
    renderTree = this.props.renderTree;
    
    return (
      <div className="App">
        <LeaseAgg />
      </div>
    );
  }
}

export default App;