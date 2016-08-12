from flask import Flask, render_template
from scrapy import current_data

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index(data=current_data):
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()
