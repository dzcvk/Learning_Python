from bottle import route, run, template, post

@route('/')
def index():
    return {"<b>Hello</b>!  <button type = 'button'> Click </button> <input type = 'submit' name = 'save' value = 'save'>"}
@post('/')
def index():
    val = request.buttons.get('button')
    return "haha"
run(host='localhost', port=8080)
