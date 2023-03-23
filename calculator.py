from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/aboutus")
def aboutUs():
    return "Welcome to the course of data science"

@app.route("/math",methods=["POST"])     #perform the calculation by submitting the forms
def math_operation():
    if(request.method=="POST"):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0
        if operation=="add":
            result=num1+num2
        elif operation=="div":
            result=num1/num2
        elif operation=="sub":
            result=num1-num2
        else:
            result=num1*num2
        return render_template("result.html",result=result)

@app.route("/operation",methods=["POST"])
def arithmatic_operation():                     #test the api through postman(http://192.168.162.79:5000/operation)
    if(request.method=="POST"):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        result=0
        if operation=="add":
            result=num1+num2
        elif operation=="div":
            result=num1/num2
        elif operation=="sub":
            result=num1-num2
        else:
            result=num1*num2
        return f"The operation is {operation} and result is {result}"

if __name__=="__main__":
    app.run(host="0.0.0.0")