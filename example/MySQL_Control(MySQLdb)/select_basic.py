import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='qq88913491',database='sedatabase')
cursor=conn.cursor()
cursor.execute('show tables')
ret=cursor.fetchall()
print(type(ret))
print(ret)
cursor.execute('select * from weibo limit 0,5')
ret=iter(cursor.fetchall())
try:
    for index in range(10):
        print(ret.__next__())
except StopIteration:
    print('end')

conn.close()

end=input('end')
