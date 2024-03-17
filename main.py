from flask import Flask, render_template
from jinja2 import environment
from draw import VigaDraw

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/iBeam')
def iBeam():
    return render_template('iBeam.html')

@app.route('/tBeam')
def tBeam():
    return render_template('tBeam.html')

@app.route('/draw')
def draw():
    image = VigaDraw(30, 60, 2, 0.63)
    print(image.CalcArmorDistante(2, 2))
    image.Plot()
    image.DrawViga(True, True)

    circles = [((15, 30), .5), ((5, 20), .5), ((25, 40), .5)]
    image.DrawMultipleArmor(circles)
    image.CalcArmorDistante(4, 12)
    graf = image.CalcArmorDistante(2,2)
    print(graf)
    return render_template('plot.html', plot=graf)
