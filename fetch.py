import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", password="", db="pymysql_console_apps", port=3306)
    id=int(input("Enter the ID of the Student : "))
    sql="SELECT * FROM student where ID ='{}'".format(id)
    cursor=con.cursor()
    cursor.execute(sql)
    res=cursor.fetchone()
    #print(res)
    print("ID : ",res[0])
    print("Name : ",res[1])
    print("Email :",res[2])
    print("Address : ",res[3])
except Exception as e:
    print(e)