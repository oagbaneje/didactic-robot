from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username = username)

@app.route('/second_home')
def second_home():
    username = request.args.get('username') 
    surname =  request.args.get('surname')
    if username and surname:
         username=username + ' ' + surname
    elif username and not surname:
        username=username
    elif not username and surname:
       username=surname
    else:
        username = 'World'
    return render_template('index2.html', username=username)

@app.route('/third_home')
def third_home():
    username = request.args.get('username') 
    surname =  request.args.get('surname')
    number_of_times = request.args.get('number_of_times')
    if number_of_times is not None and number_of_times.isdigit() is True:
        number_of_times = int(number_of_times)
    else:
        number_of_times = 1
    if username and surname:
         username = username + ' ' + surname
    elif username and not surname:
        username = username
    elif not username and surname:
       username = surname
    else:
        username = 'World'
    return render_template('index3.html', username = username, number_of_times = number_of_times)

