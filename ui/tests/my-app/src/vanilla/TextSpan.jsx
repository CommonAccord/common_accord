import React, { Component } from 'react';


class TextSpan extends Component{

    constructor(props){
        super(props);

        this.state = {
            expanded:true,
            editable:true
        }
    }


    /*
    This function recursively renders the right amount of children if 
    they exist and returns them. Called in render()
    using .map() , we turn the list of children into a series of TextSpans
    that can be rendered as html.
     */

    renderChildren(){

        if(this.props.docTree.children){

            const children = this.props.docTree.children.map( child => {

                return <TextSpan docTree={child}/> 

            });

            return children

        }else{
            return (this.props.docTree.text)
        }
    }

    
    render(){
        return (

            <span title={this.props.docTree.text} id={this.props.docTree.text}
            contentEditable={this.state.editable}>

                {this.renderChildren()}

            </span>
        );

        }
        
}



export default TextSpan;