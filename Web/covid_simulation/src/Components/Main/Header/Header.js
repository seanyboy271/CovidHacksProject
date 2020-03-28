import React, { Component } from 'react'
import './Header.css'
import Navbar from 'react-bootstrap/Navbar'
import covid from '../../../images/covidPic.png'

class Header extends Component {


    render() {
        return (
            <div className='headerContainer'>
                <Navbar bg="transparent" expand="lg" style={{ height: '100%' }}>
                    <Navbar.Brand href="#home" >
                        <div className='headerLogo'>
                            <img
                                alt=""
                                src={covid}
                                width="60"
                                height="60"
                                className="d-inline-block align-top imgSpacing"
                            />
                            <div className = 'headerLogoText'>
                                Insert Name of website here
                            </div>
                        </div>
                    </Navbar.Brand>
                </Navbar>
            </div>
        );
    }
}

export default Header




