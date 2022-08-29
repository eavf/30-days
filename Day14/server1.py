from flask import Flask


from logger import trigger_log_save
from scrape import run as scrape_runner

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=['GET'])

def hello_world():
    # run other code here
    return "Hello world. This is Flask"


# http://localhost:8000/abc
@app.route("/abc", methods=['GET'])
def abc_view():
    # run other code here
    return "Hello world. This is Flask in abc"

# http://localhost:8000/
@app.route("/box-office-mojo-scraper", methods=['POST'])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    # run other code here
    return {"data": [1,2,3,4,5,6,7]}