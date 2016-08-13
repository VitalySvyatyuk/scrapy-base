from flask import Flask, render_template
from scrapy import current_data
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'currencies.db')
db = SQLAlchemy(app)


class Currency(db.Model):
    __tablename__ = 'currencies'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    usd_rub = db.Column(db.String(8))
    eur_rub = db.Column(db.String(8))
    brent_oil = db.Column(db.String(8))
    
    def __init__(self, date, usd_rub, eur_rub, brent_oil):
        self.date = date
        self.usd_rub = usd_rub
        self.eur_rub = eur_rub
        self.brent_oil = brent_oil


@app.route("/")
def index(data=current_data):
    curr = Currency(str(datetime.now()), data['usd-rub'],
                    data['eur-rub'], data['brent-oil'])
    db.session.add(curr)
    db.session.commit()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()

