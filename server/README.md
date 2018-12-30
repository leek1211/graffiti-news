# Graffiti News Server

## Requirement

* You need to register Twitter API, Giphy API, and NewsAPI
* Save the authentication information in `config.py`
* To make git ignore the config file run `$ git update-index —assume-unchanged server/config.py`

## Install Dependencies
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install flask flask-cors newsapi-python python-twitter requests
```

## Running the server
```
$ . venv/bin/activate
$ ./run.sh
```
