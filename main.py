#this will be where the server is hosted. All other python scripts will be imported to this one.
from container import Container
from box_functions import *
from flask import Flask
app = Flask(__name__)
box = create_box()

add_item(box,"toothbrush","dental")

remove_item(box,"toothbrush")
add_item(box,"toothbrush","dental")
@app.route("/")
def home():
    return str(get_itemlocation(box,"toothbrush"))

if __name__ == "__main__":
    app.run(port = 80, host = '0.0.0.0')