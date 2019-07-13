from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "It's Magic!")

@app.route('/input', methods = ['GET', 'POST'])
def input():
    userdata = formopener.dict_from(request.form)
    name = userdata['name']
    return render_template('input.html', name = name, title = "The Magic Begins!")


@app.route('/results', methods = ['GET','POST'])
def results():
    if request.method == 'GET':
       return "You should use the form."
    else:
        userdata = formopener.dict_from(request.form)
        num1 = userdata['num1']
        num2 = userdata['num2'] 
        product = model.magicianprod(num1, num2)
        sub1 = model.magiciansub1(num1, num2)
        sub = model.magiciansub(num1, num2)
        add = model.magicianadd(num1, num2)

        print(product)
        return render_template('results.html', num1 = num1, num2=num2, product = product, sub1 = sub1, sub = sub, add = add,  title = "The Magic Ends" )