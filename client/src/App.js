import React, { Component } from "react";
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import NewsBoard from "./NewsBoard";
import Article from "./Article";

class App extends Component {
    render() {
        return(
            <div className = "App">
                <BrowserRouter>
                    <div>
                        <Switch>
                            <Route path="/" component={NewsBoard} exact />
                            <Route path="/articles" component={Article} exact />
                        </Switch>
                    </div>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;