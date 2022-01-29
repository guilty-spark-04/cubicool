#this will be where the server is hosted. All other python scripts will be imported to this one.
import container
from flask import Flask
app = Flask(__name__)
print("program finished")


@app.route("/")
def home():
    return "howdy world"

if __name__ == "__main__":
    app.run()