import React, { Component } from 'react'
import './Header.css'
import Navbar from 'react-bootstrap/Navbar'

class Header extends Component {


    render() {
        return (
            <div className='headerContainer'>
                <Navbar bg="transparent" expand="lg" style = {{height: '100%'}}>
                    <Navbar.Brand href="#home" >COVID-19</Navbar.Brand>
                </Navbar>
            </div>
        );
    }
}

export default Header




