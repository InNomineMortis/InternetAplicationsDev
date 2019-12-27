import React, { Component } from "react";
import UserRepositories from "components/UserRepositories";

class App extends Component {

    render() {
        return (
            <div>
                <UserRepositories userName="crueltycute" />
            </div>
        );
    }
}

export default App;