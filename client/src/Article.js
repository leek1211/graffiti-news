import React, { Component } from "react";

const API = "http://localhost:5000/articles";

class Article extends Component {
    constructor(props){
        super(props);

        this.state = {
            error: null,
            isLoading: false,
            articles: [],
            images: []
        };
    }

    componentDidMount() {
        this.setState({isLoading: true});
        console.log("component did mount");
        fetch(API + this.props.location.search)
            .then((res) => {
                if(res.status === 200){
                    console.log("SUCCESS");
                    return res.json();
                }else{
                    console.log(res);
                    console.log("SOMETHING WENT WRONG");
                }
            })
            .then(
                (result) => {
                    console.log("result: " + JSON.stringify(result));
                    this.setState({
                        isLoading: false,
                        articles: result.articles,
                        images: result.images
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
        const {error, isLoading, articles, images} = this.state;
        console.log(this.state);
        if(error) {
            return <div>Error: {error.message}</div>;
         }
         else if (isLoading) {
            return <div>Loading...</div>;
        } else {
            return (
                <div className="Article Header">
                    <h1>Article</h1>
                    <ul>
                        {articles && articles.map(article =>
                                <li>{article.title}</li>)
                        }
                    </ul>
                </div>
            );
        }
    }
    
}

export default Article;