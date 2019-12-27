import React, { Component } from "react";
import './style.css';

class ListRender extends Component {

    render() {
        const {item} = this.props;
        return (
            <li>{item.value}</li>
        );
    }
}

export default ListRender;