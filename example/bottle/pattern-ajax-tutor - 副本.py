from bottle import route, run, get, post, request

pattern = '''
<html><head>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function() { $('#hi_button').click(
function(){
$('#hi_result').empty()
$.ajax({ url: '/AutoManual',
 cache:false, type: 'GET',
 success: function(data) {
 $('#hi_result').append("dsf"+data.result);}
});
})
});
</script>
</head><body>

<button id='hi_button'>button hi!</button> <br><br>
<div id='hi_result'>Here will go the results of calling hi</div>


<form method = "POST">
    <input name="name" type="text" />
    <input name="password" type="password" />
    <input type="submit" value="Login" />
</form>


</body>
</html>

'''



RelayState = 0
AutoManual = 0

def GetValue(Value):
    return Value

@get('/login')
def login_form():
    return pattern

@post('/login')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    return pattern

#    if password == 'ha':
 #       return pattern%"right"
  #  else:
   #     return pattern%"wrong"
     
@get('/AutoManual')
def AutoManual():
    Value = GetValue(AutoManual)
    if(Value == 0):
        Value=1
    else:
        Value=0    
    return Value

run(host='localhost', port=8080)
