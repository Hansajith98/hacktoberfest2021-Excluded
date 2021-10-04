#''' DIGITAL CLOCK USING TKINTER'''

from tkinter import*
import time                                     # '''USING TIME MODULE TO GET SYSTEM TIME'''
root=Tk()
root.title("DIGITAL CLOCK")
root.geometry("1350x700+0+0")
root.config(bg="#081923")

def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
 #   print(h,m,s)
 #IF THIS IS NOT USED IT WILL SHOE TIME IN 24 HR CLOCK SYSTEM
    if int(h)>=12 and int(m)>0:                    #'''MAKING THE CHANGE IN AM TO PM ACCORDING TO TIME'''
        lbl_noon.config(text="PM")
    if int(h)>12:
        h=str(int((int(h)-12)))
    
    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)


# use either lucida writing or bradley handwiting
lbl_hr=Label(root,text="12",font=("lucida calligraphy",50,"bold"),bg="#087587",fg="white")
lbl_hr.place(x=350,y=200,width=150,height=150)
lbl_hr2=Label(root,text="HOUR",font=("lucida calligraphy",20,"bold"),bg="#087587",fg="white")
lbl_hr2.place(x=350,y=360,width=150,height=50)

lbl_min=Label(root,text="12",font=("lucida calligraphy",50,"bold"),bg="#008EA4",fg="white")
lbl_min.place(x=520,y=200,width=150,height=150)
lbl_min2=Label(root,text="MINUTE",font=("lucida calligraphy",20,"bold"),bg="#008EA4",fg="white")
lbl_min2.place(x=520,y=360,width=150,height=50)

lbl_sec=Label(root,text="12",font=("lucida calligraphy",50,"bold"),bg="#DF002A",fg="white")
lbl_sec.place(x=690,y=200,width=150,height=150)
lbl_sec2=Label(root,text="SECOND",font=("lucida calligraphy",20,"bold"),bg="#DF002A",fg="white")
lbl_sec2.place(x=690,y=360,width=150,height=50)

lbl_noon=Label(root,text="AM",font=("lucida calligraphy",50,"bold"),bg="#DF002A",fg="white")
lbl_noon.place(x=860,y=200,width=150,height=150)
lbl_noon2=Label(root,text="NOON",font=("lucida calligraphy",20,"bold"),bg="#DF002A",fg="white")
lbl_noon2.place(x=860,y=360,width=150,height=50)

clock()                  #CALLING FUNCTION 
root.mainloop()

#WORKING GOOD