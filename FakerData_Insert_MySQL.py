import pymysql
from faker import Faker
fake=Faker()
def myFunc():
    name = fake.name()

    email = fake.email()

    college = fake.address()
    sql = "INSERT INTO student(NAME,EMAIL,ADDRESS) VALUES ('{}','{}','{}')".format(name, email, college)
    cursor.execute(sql)
con=pymysql.connect(host="localhost",user="root",password="",db="pymysql_console_apps",port=3306)

cursor=con.cursor()


for i in range(1,100+1,1):
    myFunc()
print("Data Inserted")
con.commit()
con.close()