import React, { Component } from 'react';

class TextSpan extends Component{
    /*
    This function recursively renders the right amount of children if 
    they exist and returns them. Called in render()
    using .map() , we turn the list of children into a series of TextSpans
    that can be rendered as html.
     */

    render(){
      return (
        <span title={this.props.text} id={this.props.text}
        contentEditable={this.props.editable} onDoubleClick={this.props.clickHandler}
        dangerouslySetInnerHTML={{ __html: this.props.text }} />

      );
    }
    
}



export default TextSpan;