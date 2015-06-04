from bottle import Bottle, run, template
app = Bottle()
@app.route('/')
def hello():
    return template("<h1> Hello {{name}} World! </h1>", name = "Pei's")

@app.route('/python')
def hello():
    return "<h1> Hello Python! </h1>"

run(app, host='localhost', port=8080)
