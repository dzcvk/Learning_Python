import psycopg2

connection = psycopg2.connect(database = "EleDevicesDB",
                              user = "postgres",
                              password = "qq88913491",
                              host = "localhost",
                              port = "5432")

########### Create a table ###########
cur = connection.cursor()
cur.execute("CREATE TABLE DiodeTbl (ID INT PRIMARY KEY NOT NULL, DeviceName TEXT NOT NULL, Umax INT);")
connection.commit()
connection.close()
