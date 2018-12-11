import React, { Component } from 'react';
import Literal from './Literal'
import ReactDOM from 'react-dom';

class TextSpan extends Component{

    constructor(props){
        super(props);

        this.state = {
            expanded:true,
            editable:false
        }
    }

    handleClick = (e) => {
        // toggle the state of thi component
        this.setState({
            editable: !this.state.editable,
            expanded: !this.state.expanded
        });
    }

    /*
    This function recursively renders the right amount of children if 
    they exist and returns them. Called in render()
    using .map() , we turn the list of children into a series of TextSpans
    that can be rendered as html.
     */

    renderChildren() {
        
        if(this.props.docTree.children){
            
            const children = this.props.docTree.children.map( child => {
                if (child.children) {
                    return <TextSpan docTree={child} ref={child.text}/> 
                } else {
                    return <Literal text={child.text} clickHandler={this.handleClick}
                        editable={this.state.editable} />
                }
            });

            return children
        } else {
            return (this.props.docTree.text)
        }
    }


    render(){
        if (this.state.expanded) {
            return (
                <span title={this.props.docTree.text} id={this.props.docTree.text}
                contentEditable={this.state.editable}>

                    {this.renderChildren()}

                </span>
            );
        } else {
            return (
                <span title={this.props.docTree.text} id={this.props.docTree.text}
                contentEditable={this.state.editable} onDoubleClick={this.handleClick}> 
                {this.props.docTree.text}
                </span>
            );
        }

        }
        
}



export default TextSpan;