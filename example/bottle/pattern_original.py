from bottle import route, run, get, post, request

pattern = '''


<form method = "POST">
    <input name="name" type="text" />
    <input name="password" type="password" />
    <input type="submit" value="Login" />
    <input type="submit" value="Ha" />
</form>
<input name="show" type="text" value="%s" />


'''

@get('/login')
def login_form():
    return pattern%""

@post('/login')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if password == 'ha':
        return pattern%"right"
    else:
        return pattern%"wrong"
     
    
run(host='0.0.0.0', port=8080)
