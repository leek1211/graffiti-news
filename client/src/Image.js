import React, { Component } from "react";

class Image extends Component {
    constructor(props){
        super(props);

        this.randomize = this.randomize.bind(this);
    }

    randomize(images){
        let array = images;
        let ret = [];

        for(let i = 0; i < 3; i++){
            let size = array.length;
            let random = Math.random();
            let index = parseInt(size * random);
            
            ret.push(images[index]);
            array.splice(index, 1);
        }
        return ret;
    }

    render() {
        return(
            <div onClick={this.props.onClick}>
                <div>{this.props.keyword}</div>
                {this.randomize(this.props.images).map(image =>
                    <a href = {'/articles?keyword='+ this.props.keyword} ><img src = {image.url}/></a>
                )}
            </div>
        );
    }
}

export default Image