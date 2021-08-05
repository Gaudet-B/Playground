from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template("play.html")
@app.route('/play/<int:boxes>')
def number_of_boxes(boxes):
    return render_template("play.html", boxes=boxes)
@app.route('/play/<int:boxes>/<string:color>')
def box_color(boxes, color):
    return render_template("play.html", boxes=boxes, color=color)
if __name__=="__main__":
    app.run(debug=True)