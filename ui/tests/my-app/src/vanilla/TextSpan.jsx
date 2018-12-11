import React, { Component } from 'react';


class TextSpan extends Component{

    constructor(props){
        super(props);

        this.state = {
            expanded:true,
            editable:false
        }
    }


    /*
    This function recursively renders the right amount of children if 
    they exist and returns them. Called in render()
    using .map() , we turn the list of children into a series of TextSpans
    that can be rendered as html.
     */

    renderChildren(){


        const children = this.props.docTree.children.map( child => {

            if(child.children){ //if the child has children

                return <TextSpan docTree={child}/>;

            }
            return <span dangerouslySetInnerHTML={{ __html: child.text }} /> ;


        });

        return children
    }


    /*
    Manages what happens to the span when it is double clicked
    */
    onDblClick = (event) => {
        this.setState({editable: true})
    }


    render(){
        return (

            <span title={this.props.docTree.text} id={this.props.docTree.text}
            contentEditable={this.state.editable} onDoubleClick={this.onDblClick} >

                {this.renderChildren()}

            </span>
        );

        }
        
}



export default TextSpan;