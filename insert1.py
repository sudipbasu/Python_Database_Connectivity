import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",db="pymysql_console_apps",port=3306)
    name=input("Enter the name : ")
    email=input("Enter the Email : ")
    college=input("Enter the College : ")
    cursor_var=db.cursor()
    sql="INSERT INTO student(NAME,EMAIL,COLLEGE) VALUES ('{}','{}','{}')".format(name,email,college)
    cursor_var.execute(sql)
    db.commit()
    db.close()
    print("Data Added :)")
except Exception as e:
    print(e)
