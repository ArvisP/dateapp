from . import app
import datetime
from flask import request
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculated")
def calc():
    if request.args:
        date = request.args.get("date")
        year, month, day = (int(x) for x in date.split('-'))
        ans = datetime.date(year, month, day)
        month_lst = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
        answer = ans.strftime("%A") +", "+month_lst[month-1]+" "+str(day)+", "+str(year)

        return render_template("index.html", result=answer)
    else:
        return render_template("index.html")
