#this will be where the server is hosted. All other python scripts will be imported to this one.
from container import Container
from box_functions import *
from flask import Flask, render_template, request
app = Flask(__name__)
box = create_box()

add_item(box,"toothbrush","dental")

remove_item(box,"toothbrush")
add_item(box,"toothbrush","dental")
@app.route("/", methods = ['GET','POST'])
def index():
    return render_template("gui.html")

@app.route("/home", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['checker'] == "add":
            item = request.form['item']
            category = request.form['cata']
            add_item(box,item,category)
        elif request.form['checker'] == 'remove':
            item = request.form['item']
            remove_item(box,item)
        return render_template("gui.html")
    else:
        return render_template("display.html", box = box)
# @app.route("/home", methods = ['POST'])
# def get_add():
#     item = request.form['item']
#     category = request.form['cata']
#     add_item(box,item,category)
#     return render_template("display.html", box=box)

if __name__ == "__main__":
    app.run(port = 80, host = '0.0.0.0')