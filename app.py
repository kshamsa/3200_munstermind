from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

import numpy as np 

@app.route('/')
def hello_world():
    return render_template('munstermind.html')



@app.route('/checkguess', methods={'POST'})
def checkguess():
    print('in check guess')
    print(request.json) #print out the json object to the console
    print(request.json['guess']) #print out the guess to the console
    print(request.json['enigma']) #print out the enigma to the console
    guess_list = request.json['guess']
    enigma_list = request.json['enigma']
    print("TEST OUT DATA BELOW HERE/////////////////////////////")
    print(guess_list)
    print(enigma_list)
    #Hey student: your code here!!!!

    guess = np.asarray(guess_list)
    enigma = np.asarray(enigma_list)
    results = ["","","",""]
    whitePegs = 0 #black is a match
    blackPegs = 0 #color exists but its in the wrong index
    index = 0

    for s in guess:
        if s == enigma[index]:
            whitePegs = whitePegs + 1
            results[index] = "blackPeg"
        
        index = index + 1
    
    for s in guess:
        if s in enigma_list:
            if results[enigma_list.index(s)] != "blackPeg":
                results[enigma_list.index(s)] = "whitePeg"
                whitePegs = whitePegs + 1

    print("whitePegs")
    print(whitePegs)
    print("blackPegs")
    print(blackPegs)           
    
    hint = {'whitePegs':whitePegs, 'blackPegs':blackPegs} #create the hint as a dict
    print("the hint:", hint) #print out the hint to the console
    return jsonify(hint) #return the dict as a json


@app.route('/tinker_json')
def bar():
    # see https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
    ]
    return jsonify({'tasks': tasks})
