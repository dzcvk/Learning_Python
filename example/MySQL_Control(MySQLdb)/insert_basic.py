import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='qq88913491',database='sedatabase')
cursor=conn.cursor()
cursor.execute('show tables')
ret=cursor.fetchall()
print(type(ret))
print(ret)
cursor.execute('insert into ')
ret=iter(cursor.fetchall())

conn.close()

end=input('end')
