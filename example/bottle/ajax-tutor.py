from bottle import route, run, get, post, request, template

RelayState = 0
AutoManualState = 0

def GetValue(Value):
    return Value

@route('/')
def Home():
    return template('Home.txt')

@route('/AutoManual', method='GET')
def AutoManual():
    global AutoManualState
    if(AutoManualState==0):
        AutoManualState=1
    else:
        AutoManualState=0
    print("AutoManual: "+str(AutoManualState))
    return {'AutoManualState':AutoManualState}

@route('/RunStop')
def RunStop():
    global RelayState
    if(RelayState == 0):
        RelayState=1
    else:
        RelayState=0
    print("RunStop: "+str(RelayState))
    return {"RelayState":RelayState}

@route('/Refresh')
def Refresh():
    global AutoManualState
    return {"AutoManualState":AutoManualState,"RelayState":RelayState}

#@route('/RefreshRelayState')
#def RefreshRelayState():
#    global RelayState
#    return {"RelayState":RelayState}
    
    
run(host='localhost', port=8080)
