from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", 
    numeber1=12, number2=15)

@app.route("/karil")
def calculer():
    num1, num2 = 23,45
    return render_template(calcule.html, value1=num1, value2=num2, 
    value3=num1*num2)

if __name__=="__main__":
    #app.run(host='0000',port=80)
    app.run(debug=True)
    