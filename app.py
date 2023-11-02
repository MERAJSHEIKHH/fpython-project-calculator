
from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template("index.html")

 
@app.route("/math", methods=["POST"])
def calculator_test():
    ops=request.form.get("operation")  
    first_num= int(request.form.get("num1"))
    second_num=int(request.form.get("num2"))

    if (ops=="add"):
        r=first_num+second_num
        return f"addition of {first_num} and {second_num}are {r}"

    if ops==("subtract"):

        r=first_num-second_num
        return f"substraction of {first_num} and {second_num}are {r}"

    if (ops=="multiply"):
        r=first_num*second_num
        return f"multiplication of {first_num} and {second_num}are {r}"

    if (ops=="divide"):
        r=first_num/second_num
        return f"division of {first_num} and {second_num}are {r}"


if __name__=="__main__":
    app.run(host="0.0.0.0")



