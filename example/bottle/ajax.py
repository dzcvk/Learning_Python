from bottle import route, run, get, post, request, template

RelayState = 0
AutoManualState = 0

def GetValue(Value):
    return Value

@route('/')
def Home():
    return template('Home.txt')

@route('/AutoManual')
def AutoManual():
    global AutoManualState
    if(AutoManualState==0):
        AutoManualState=1
    else:
        AutoManualState=0
    print("AutoManual: "+str(AutoManualState))
    return str(AutoManualState)

@route('/RunStop')
def RunStop():
    global RelayState
    if(RelayState == 0):
        RelayState=1
    else:
        RelayState=0
    print("RunStop: "+str(RelayState))
    return str(RelayState)

@route('/RefreshAutoManual')
def RefreshAutoManual():
    Value = GetValue(AutoManual)
    return Value

@route('/RefreshRelayState')
def RefreshRelayState():
    Value = GetValue(RelayState)
    return Value
    
    
run(host='localhost', port=8080)
