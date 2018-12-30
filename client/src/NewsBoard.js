import React, { Component } from "react";

const API = "http://localhost:5000/graffiti";

class NewsBoard extends Component {
    constructor(props){
        super(props);
        
        this.state = {
            error: null,
            isLoading: false,
            trends: []
        };
    }
    
    componentDidMount() {
        this.setState({isLoading: true});

        console.log("component did mount");
        
        fetch(API)
            .then((res) => {
                if(res.status === 200){
                    console.log("SUCCESS");
                    return res.json();
                }else if(res.status === 408){
                    console.log("SOMETHING WENT WRONG");
                }
            })
            .then(
                (result) => {
                    this.setState({
                        isLoading: false,
                        trends: result.trends
                    });
                    console.log(this.state.isLoading);
                    console.log("DATA STORED");
                },
                // Handle errors here
                (error) => {
                    this.setState({
                        isLoading: false,
                        error
                    });
                }
             )
    }

    render() {
        const {error, isLoading, trends} = this.state;
        if(error) {
            return <div>Error: {error.message}</div>;
         }
         else if (isLoading) {
            return <div>Loading...</div>;
        } else {
            return (
                <div className = "NewsBoardMain">
                    <ul>
                        {trends && trends.map(trend => (
                            <li key = {trend.keyword}>
                                {trend.keyword} {trend.url}
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }

}

export default NewsBoard;