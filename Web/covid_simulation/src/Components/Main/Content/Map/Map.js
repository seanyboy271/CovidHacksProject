import React, { Component } from 'react'
import GoogleMapReact from 'google-map-react';
import './Map.css'
const AnyReactComponent = ({ text }) => <div>{text}</div>;


export default class Map extends Component {

    constructor(props) {
        super(props);
        this.state = {
            key: 'AIzaSyCRNizak5tpP7S_LA_JPg_joPifTKmaQzw',
            heatMapData: [{ x: 10, y: 15, value: 5 }, { x: 50, y: 50, value: 2 }]
        }
    }

    render() {
        return (
            <div className='heatMap'>
                {console.log(this.state.heatMapData)}
                <GoogleMapReact
                    bootstrapURLKeys={{ key: this.state.key }}
                    defaultCenter={[34.0522, -118.2437]}
                    defaultZoom={10}
                >
                    <AnyReactComponent
                        lat={34.0522}
                        lng={-118.2437}
                        text="My Marker"
                    />
                </GoogleMapReact>
            </div>
        );
    }
}
