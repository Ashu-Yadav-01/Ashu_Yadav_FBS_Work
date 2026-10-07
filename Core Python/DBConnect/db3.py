import mysql.connector
try:
    con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="emp"
    )
except Exception as e:
    print("Problem  in DB conect ",e)
if con.is_connected:
    print("I am done with Db")
cursor=con.cursor()
id=input("enter the id= ")
name=input("Enter  the name ")
# qury=f"insert into employee values ({id},'{name}')"
# cursor.execute(qury)
# q="insert into employee(id,ename) values(%s,%s)"
# value=(id,name)
# cursor.execute(q,value)
# con.commit()
# qur="update employee set ename='Harman' where id=12"
qur="delete from employee where id=12"
cursor.execute(qur)
con.commit()
# cursor.execute("Select * from Employee")
# print(cursor.fetchone())
# # rows=cursor.fetchmany(4)
# rows=cursor.fetchall()
# print(rows)
con.close()
