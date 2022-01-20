# Import Flask
from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # return '<h1>Hello world</h1>'
    # Plantilla HTML debe estar en directorio templates
    hobbies = ['Read', 'Sing']
    return render_template("index.html", name = "Mitchell", lastname = "Rodríguez", hobbies = hobbies)

# Register helloName function with route decorator
@app.route('/<name>', methods=['GET'])
def helloName(name):
    return '<h1>Hello {}</h1>' . format(name)

@app.route('/data/<name>/<lastname>', methods=['GET'])
def printData(name, lastname):
    return '<h1>Hello {} {}</h1>' . format(name, lastname)

users = [{
    "name": "Alex",
    "lastname": "Martinez",
    "id": 123
},
{
    "name": "Martha",
    "lastname": "Sanchez",
    "id": 456
},
{
    "name": "Ruben",
    "lastname": "Castro",
    "id": 789
},
]

@app.route('/users/<int:id>', methods=['GET'])
def printUserData(id):
    print(type(id))
    userFound = None
    for user in users:
        if user["id"] == id:
            userFound = user
    return render_template("user.html", user = userFound, id = id)


if __name__ == "__main__":
    app.run( debug = True )