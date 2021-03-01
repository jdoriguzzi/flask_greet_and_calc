from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_nums():
    """Do addition on a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a,b))

@app.route("/sub")
def sub_nums():
    """Do subtraction on a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a,b))

@app.route("/mult")
def mult_nums():
    """Do multiplication on a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a,b))

@app.route("/div")
def div_nums():
    """Do division on a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a,b))



############ All-in-one code:

ops = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<op>")
def do_math(op):
    """Do given operation on a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(ops[op](a, b))