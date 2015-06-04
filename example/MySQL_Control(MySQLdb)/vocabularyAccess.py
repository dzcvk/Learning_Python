import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='qq88913491',database='lingodatabase')
cursor=conn.cursor()

table='eng_vocabulary'
items='vocabulary,affix,remark'

while True:
    data=input('please type the vocabulary,affix and remark in,and split them with ";" in:\n>>')
    if data == 'runout':
        break
    else:
        raw=data.split(';')
        values="'"+str(raw[0])+"'"+','+"'"+str(raw[1])+"'"+','+"'"+str(raw[2])+"'"
        sqlDirect='insert into %(table)s (%(items)s) values(%(values)s)'%{'table':table,'items':items,'values':values}
        print(sqlDirect)
        try:
            cursor.execute(sqlDirect)
        except:
            print('error')
        conn.commit()

conn.close()
end=input('exited')
