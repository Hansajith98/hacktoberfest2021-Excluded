# STACKS AND OPERATIONS ON STACKS

l=[]
n=int(input("ENTER THE NO OF ELEMENTS:"))
for i in range(n):
    a=input("ENTER THE ELEMENT:")
    l.append(a)
print(l)

#DEFINING EMPTY STACK 

def emptystk(stk):
    if stk==[]:
        return True
    else :
        return False
    
#ADDIND MORE ELEMENTS

def push(stk,x):
    stk.append(x)
    top =len(stk)-1
    
#DELETING ELEMENTS FROM TOP

def pop(stk):
    print("BY DEFAULT THE POPPED ITEM IS THE TOPMOST ITEM")
    if emptystk(stk):
        print("UNDERFLOW")
    else:
        x=stk.pop()
        if len(stk)==0:
            top =None
        else:
            top=len(stk)-1
        return x
        
    
#DISPLAYING THE TOPMOST ELEMENT

def peek(stk):
    if emptystk(stk):
        print("UNDERFLOW")
    else:
        top=len(stk)-1
        return stk[top]
    
#DISPLAYING THE WHOLE LIST

def display(stk):
     if emptystk(stk):
        print("STACK IS EMPTY")
     else:
        top=len(stk)-1
        print(stk[top],"\t <-TOP")
        for i in range(top-1,-1,-1):
            print(stk[i])
            


top = None
while True:
    print("-----------------------------------------------------------------------------")
    print("OPERATIONS")
    print("1.PUSH")
    print("2.POP")   
    print("3.PEEK")
    print("4.DISPLAY")
    print("5.EXIT")
    print("-----------------------------------------------------------------------------")
    
    op=input("ENTER THE NUMBER TO PERFORM OPERATION:")
    if op=="1":
        x=input("ENTER ELEMENT:")
        push(l,x)
    elif op=="2":
        x=pop(l)
        if x =="UNDERFLOW":
            print("EMPTY STACK")
        else:
            print("POPPED ITEM IS",x)
    elif op=="3":
        x=peek(l)
        if x=="UNDERFLOW":
            print("EMPTY STACK")
        else:
            print("TOPMOST ITEM IS",x)
            
    elif op=="4":
        print("COMPLETED READING STACKS")
        print("BELOW THE STACK IS DISPLAYED")
        display(l)
    elif  op=="5":
        print("THANK YOU ")
        print("OPERATIONS ENDED")
        break
    else:
        print("INVALID OPERATION ")
        
display(l)