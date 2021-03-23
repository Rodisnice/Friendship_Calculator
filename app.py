from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name1 = request.form["name1"]
        name2 = request.form["name2"]
        percentage = random.randint(0, 101)
        result = name1 + " and " + name2 + " like eachother " + str(percentage) + "%"
        return render_template("index.html", content=result)
    return render_template("Index.html")

