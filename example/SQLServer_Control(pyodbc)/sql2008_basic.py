def accessSqlServer(serverName,portNum,databaseName,userName,password,tableName):
	connStr=''
	connStr+='DRIVER={SQL Server};'
	connStr+='SERVER='+serverName+','+portNum+';'
	connStr+='DATABASE='+databaseName+';'
	connStr+='UID='+userName+';'
	connStr+='PWD='+password

	try:
		conn=pyodbc.connect(connStr)
	except:
		return False

	try:
		