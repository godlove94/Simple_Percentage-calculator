from flask import Flask, render_template, request
import math 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message = 'Welcome')
    else:
        var1 = request.form['fnumber']
        var2 = request.form['vnumber']
        var3 = float(var1)
        var4 = float(var2)
        var5 = float(100)
        var6 = var4 / var5
        var7 = var6 * var3
        message = 'the result is ' + str(var7)
        return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
