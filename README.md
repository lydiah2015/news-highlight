News Highlight
==============

**Author**: [Lydia Mitchelle Makini](https://github.com/lydiah2015)
## Description
[News Highlight](:https://github.com/lydiah2015/news-highlight.git) is a web appliction that displays a list of entertainment news sources from around the world. A user is able to click on a news source and view a list of articles from that source. Clicking on the news article will then redirect you to the news article's web page.

## Installation

### Requirements
* Python 3.6.4

### Cloning the repository
```bash
git clone :https://github.com/lydiah2015/news-highlight.git && cd news-highlight
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip install -r requirements
```

### Running Tests
```bash
python -m unittest tests/test_models.py
```

### Running in development
```bash
python run.py
```
Open the app on your browser, by default on `127.0.0.1:5000`.

### Deploying to heroku
- Make sure you have  `requirements.txt`
```bash
#should be in virtual
pip freeze > requirements.txt
```
- create a `Procfile` with the following content
```Procfile
web: gunicorn 'app:create_app()' --access-logfile - --error-logfile -
```
- If **deploying for the first time**, make sure you have `heroku cli` installed then create app by running
```bash
heroku create appname
```
- Make sure you have committed all changes then run
```bash
git push heroku master
```

## Live Demo

The web app can be accessed from the following link
[https://entertainment-news-highlight.herokuapp.com/](https://entertainment-news-highlight.herokuapp.com/)

## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Known Bugs 

There are no known bugs. If you find any be sure to create an issue 


## License ##
This project is licensed under the MIT Open Source license, (c) [ Lydia Mitchelle Makini](https://github.com/lydiah2015)