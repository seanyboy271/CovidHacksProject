import React, { Component } from 'react'
import './Main.css'
import axios from 'axios';

class Main extends Component {

    constructor(props) {
        super(props)
        this.state = {
            apiCall: "Not yet called"
        }
    }


    componentDidMount(){
        this.testAPICall()
    }
    
    async testAPICall(){
        let cors = 'http://127.0.0.1:8080/'
        let url = '127.0.0.1:5000/'
        let response =  await axios.get(cors+url)
        console.log('REsponser', response)
        this.setState({
            apiCall: response.data
        })
    }

    render() {
        return (
            <div className = 'mainContainer'>
                Hello from main Component
                <br/>
                API test call: {this.state.apiCall}
            </div>

        );
    }
}

export default Main




