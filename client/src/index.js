import React from "react";
import ReactDOM from "react-dom";
import NewsBoard from "./NewsBoard";
import "./index.css";

var destination = document.querySelector("#container");

ReactDOM.render (
    <div>
        <NewsBoard />
    </div>,
    destination
);