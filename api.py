# from flask import Flask

# app = Flask("demo")

# @app.route('/home')
# def mufun():
#     return "{'Name' : 'Tanish}"

# app.run(debug=True)

from flask import Flask, jsonify

app = Flask("demo")

@app.route('/users/<string:n1>', methods=['POST' , 'GET'])
def mufun(n1):
    n1 = "Hello " + n1
    return jsonify({'output' : n1})

    # http://127.0.0.1:5000/users/CS101 link

app.run(debug=True)

