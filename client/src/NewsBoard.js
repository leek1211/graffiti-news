import React, { Component } from "react";
import Image from "./Image";

const API = "http://localhost:5000/graffiti";

class NewsBoard extends Component {
    constructor(props){
        super(props);
        
        this.state = {
            error: null,
            isLoading: false,
            trends: []
        };
        //this.imageOnClick = this.imageOnClick.bind(this);
    }
    
    componentDidMount() {
        this.setState({isLoading: true});
        console.log("component did mount");
        
        fetch(API)
            .then((res) => {
                if(res.status === 200){
                    console.log("SUCCESS");
                    return res.json();
                }else{
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

    /*imageOnClick(keyword) {
        console.log(keyword);
    }*/

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
                    <div className = "NewsBoard Header">
                        <h1>Graffiti News</h1>
                    </div>
                    {trends && trends.map(trend => 
                        <Image key={trend.keyword} 
                            images={trend.images} 
                            keyword={trend.keyword} 
                            /*onClick={() => this.imageOnClick(trend.keyword)}*/ />
                    )}
                </div>    
            );
        }
    }

}

export default NewsBoard;