import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashu1234",
    database="Ashu_1"
)

if con.is_connected():
    print("Done")

cur = con.cursor()


query = 'insert into employee values (18, "Virat")'

cur.execute(query)
con.commit()

q = "select * from employee"
cur.execute(q)


row = cur.fetchone()
row = cur.fetchall()
#rows =cur.fetchmany(3)

print(row)