import mysql.connector as sq
mydb=sq.connect(host="localhost",user="root",passwd="adityakumar1234",database="aditya")
print("Connection established")
cur=mydb.cursor()
cur.execute("CREATE TABLE DOC (rollno int(5),name varchar(15),class varchar(2),city varchar(10))")
ch='y'
while ch=='y' or ch=='Y':
    rollno=input("Roll number:")
    name=input("Enter name:")
    Class=input("Enter class:")
    city=input("Enter city:")
    cur.execute("INSERT INTO DOC VALUES('"+rollno+"','"+name+"','"+Class+"','"+city+"')")
    mydb.commit()
    ch=input("Do you want to add more?:")
    
