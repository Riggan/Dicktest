from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

sizes = []
global s,c, avg
s=6
c=0
avg=7
s=float(s)

@app.route("/", methods=["GET","POST"])
def index():
    global s,c,avg

    c = c+1
    if request.method == "POST":
        size = request.form.get("size")
        size=float(size)
        s = s + size
        avg = s/c
        if size>avg:
            return render_template("index.html", comment="More than average",avg=avg)
        elif size<avg:
            return render_template("index.html", comment="Less than average",avg=avg)
        elif size==avg:
            return render_template("index.html", comment="Average",avg=avg)
    return render_template("index.html", comment="Average",avg=avg)

if __name__ == '__main__':
    app.run(debug = True)
