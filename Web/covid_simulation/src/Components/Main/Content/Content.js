import React, { Component } from 'react'
import './Content.css'
import Map from './Map/Map.js'
const AnyReactComponent = ({ text }) => <div>{text}</div>;


class Content extends Component {


    render() {
        return (
            <div className='contentContainer'>
                <div className='leftSidebar'>
                    this is the left sidebar
                </div>
                <Map />
            </div>
        );
    }
}

export default Content




