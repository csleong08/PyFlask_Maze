from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/firstLeft')
def firstLeft():
    return render_template('firstLeft.html')

@app.route('/firstRight')
def firstRight():
    return render_template('firstRight.html')

@app.route('/secondLeft')
def secondLeft():
    return render_template('secondLeft.html')

@app.route('/secondRight')
def secondRight():
    return render_template('secondRight.html')

@app.route('/thirdLeft')
def thirdLeft():
    return render_template('thirdLeft.html')

@app.route('/thirdRight')
def thirdRight():
    return render_template('thirdRight.html')

app.run(debug=True)