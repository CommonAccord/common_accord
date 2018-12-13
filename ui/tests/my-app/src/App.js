import React from 'react'
import TextSpan from './vanilla/TextSpan.jsx'

const docTree = {text: 'Prose Description', 
  metadata: {path: [], names: []}, children: [
    

    {text: ''}, 
    
    {text: 'Buyer.Name', 
    metadata: {path: [], names: []}, 
    children: [
                   
      {text: 'Alice'}

    ]},
    
    {text: ' bought a book for '},
    
    {text: 'Buyer.Friend.2.Name', 
    metadata: {path: [], names: []}, 
    children: [
      
      {text: 'Rob'}
    
    ]},
    
    {text: '. <br> It was called '},
    
    
    {text: 'Item.Book.Title', 
    metadata: {path: ['Item.Book.'], names: ['Moby_Dick']}, 
    children: [
      
      {text: 'Moby Dick'}
    
    ]},
    
    {text: ' by '},
    
    {text: 'Item.Book.Author',
    metadata: {path: ['Item.Book.'], names: ['Moby_Dick']},
    children: [
      
      {text: 'Herman Melville'}
    
    ]}, 
    
    {text: '. She sent it in the mail to '},
    
    {text: 'Buyer.Friend.2.Name_and_Address.Formal', 
    metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']},
    children: [
      
      {text: ''},
      
      {text: 'Full Name', 
      metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']}, 
      children: [
        
        {text: ''},

        {text: 'First Name', 
        metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']},
        children: [
          
          {text: 'Robert'}
        ]}, 
        
        {text: ' '},
        
        {text: 'M.I.', 
        metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']}, 
        children: [

          {text: 'F.'}
        
        ]}, 
        
        {text: ' '},
        
        {text: 'Last Name',
        metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']},
        children: [
          
          {text: 'Mueller'}
        ]},
        
        {text: ''}
      
      ]}, 
      
      {text: ', '},
      
      {text: 'Address',
      metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']},
      children: [
        
        {text: ''}, 

        {text: 'Address.FirstLine',
        metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']},
        children: [
          
          {text: '13 Benefit St.'}
        
        ]}, 
        
        {text: ','},
        
        {text: 'Address.City', 
        metadata: {path: ['Buyer.', 'Friend.2.'], names: ['Alice', 'Bob']}, 
        children: [
          
          {text: 'Providence'}
        
        ]}, 
        
        {text: ', '},
        
        {text: 'State', 
        metadata: {path: ['Buyer.'], names: ['Alice']}, 
        children: [
          
          {text: 'Rhode Island'}
        
        ]}, 
        
        {text: ''}
      
      ]}, 
      
      {text: ''}
    
    ]}, 
    
    {text: '.'}
  
  ]}


class App extends React.Component {


  state = {

  }


  render() {
    
    return(

      <div>
      <TextSpan docTree={docTree}/>
      </div>

      )
  }

}

export default App;

