'''TO ENTER BOOKS OF  VARIOUS SUBJECT AND PERFORM MULTIPLE OPERATIONS'''

def write_books():
    op="y"
    while op=="y":
        sub=input("ENTER THE SUBJECT:")
        bname=input("ENTER THE BOOK NAME:")
        auth=input("ENTER THE AUTHOR:")
        price=input("ENTER THE PRICE:")
        op=input("WANT TO CONTINUE:")
    
        l=[]
        l.append(sub)
        l.append(bname)
        l.append(auth)
        l.append(price)
    
        f=open(fname,"a")
        f.write("\n")
        f.write(str(l))
        f.close()
    
def read():
    l1=[]
    sub1=input("ENTER THE SUBJECT:")
    f=open(fname,"r")
    for i in f:
        if sub1 in i:
            l1=eval(i)           
            print("subject:",l1[0])
            print("Book:",l1[1])
            print("Author:",l1[2])
            print("Price:",l1[3])
    f.close()
    
print("HELLO!! ADD AS MUCH BOOKS YOU WANT")
do=input("1.want to add books OR 2.find books:")
fname=input("ENTER THE FILE NAME:")
addbooks=["1","add","add books"]
findbooks=["2","find","find books"]
if do in addbooks:
    write_books()
elif do in findbooks:
    read()
else:
    print("ok ended the program")
    print("THANK YOU")    