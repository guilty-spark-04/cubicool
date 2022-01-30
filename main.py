#this will be where the server is hosted. All other python scripts will be imported to this one.
from container import Container
from box_functions import *
from flask import Flask
app = Flask(__name__)
box = create_box()

box[7].add_item("toothbrush","dental")


@app.route("/")
def home():
    return str(get_categoryLocation(box,"dental"))

if __name__ == "__main__":
    app.run()