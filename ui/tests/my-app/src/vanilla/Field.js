import React, { Component } from 'react';


class Field extends Component{
    /*

    */
    constructor(props){
        super(props)
        
        this.state = {
            expanded: true,
            value: props.value
        };
    }
    
    handleChange(event) {
        // append value of keypress to this.state.value
        this.setState({value: event.target.value})
    }
    
    // handles single and double click
    handleClicks = () => {
        if (this.clickTimeout !== null) {
            // double click
            clearTimeout(this.clickTimeout)
            this.clickTimeout = null
            this.this.setState({expanded: !this.state.expanded})
        } else {
            // single click
            this.clickTimeout = setTimeout(() => {
                // first click executes
                clearTimeout(this.clickTimeout)
                this.clickTimeout = null
            }, 2000)
        }
    }

    render(){
        // Need some logic to dynamically adjust the size of the text boxes
        if (this.state.expanded) {
            return (<input id="1" type="text" value={this.state.value} 
                onchange={this.handleKeyPress} />);
        } else {
            return (<input id="1" type="text" value={this.props.key} 
                onchange={this.handleKeyPress} />);
        }
    }
}



export default Field;