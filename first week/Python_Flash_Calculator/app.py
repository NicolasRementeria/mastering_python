from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')

def main():
    return render_template('app.html') 

@app.route('/send', methods=['POST'])

@app.route('/sendEquation', methods=['POST'])

def send(sum=sum):
    if request.method == 'POST':
        
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
    
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'substract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'exponential':
            sum = float(num1) ** float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'logarithm':
            sum = math.log(float(num1), float(num2))
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')

def sendEquation(sumEquation=sum):
    if request.method == 'POST':
        equation = request.form['equation']
        if equation:
            sumEquation = float(equation)
            return render_template('app.html', sum=sumEquation)

if __name__ == ' __main__':
    app.debug = True
    app.run()