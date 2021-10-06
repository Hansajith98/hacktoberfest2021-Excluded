from tkinter import *
import random
import base64
window = Tk()
window.geometry("1200x600")
window.title("ENCRYPT/DECRYPT MESSAGE WINDOW")  
Tops = Frame(window, width = 1600, relief = RIDGE)
Tops.pack(side = TOP)
f1 = Frame(window, width = 800, height = 700, relief = RIDGE)
f1.pack(side = TOP)
lblInfo = Label(Tops, font = ('Lucida Console', 50, 'bold'), text = "\nENCRYPT/DECRYPT MESSAGE\n\n", fg = "Black", bd = 10, anchor='w')   
lblInfo.grid(row = 0, column = 0)

Msg = StringVar()
psd = StringVar()
mode = StringVar()
Result = StringVar()

# labels
lblMsg = Label(f1, font = ('Times New Roman', 16, 'bold'), text = "MESSAGE", bd = 16, anchor = "w")

lblMsg.grid(row = 0, column = 0)    

txtMsg = Entry(f1, font = ('Times New Roman', 16, 'bold'), textvariable = Msg, bd = 10, insertwidth = 4, bg = "white", justify = 'right')
        
txtMsg.grid(row = 0, column = 1)

lblpsd = Label(f1, font = ('Times New Roman', 16, 'bold'), text = "PASSWORD KEY", bd = 16, anchor = "w")
        
lblpsd.grid(row = 1, column = 1)

txtpsd = Entry(f1, font = ('Times New Roman', 16, 'bold'), textvariable = psd, bd = 10, insertwidth = 4, bg = "white", justify = 'right')

txtpsd.grid(row = 1, column = 2)

lblmode = Label(f1, font = ('Times New Roman', 16, 'bold'), text = "MODE(e - Encrypts, d - Decrypts)", bd = 16, anchor = "w")
        
lblmode.grid(row = 2, column = 1)

txtmode = Entry(f1, font = ('Times New Roman', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, bg = "white", justify = 'right')
        
txtmode.grid(row = 2, column = 2)

lblService = Label(f1, font = ('Times New Roman', 16, 'bold'), text = "Resulted Message", bd = 16, anchor = "w")

lblService.grid(row = 0, column = 3)

txtService = Entry(f1, font = ('Times New Roman', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4, bg = "white", justify = 'right')

txtService.grid(row = 0, column = 4)

def encode(psd, clear):                                                  # encode function
    enc = []
    for i in range(len(clear)):
        psd_c = psd[i % len(psd)]
        enc_c = chr((ord(clear[i]) + ord(psd_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
  
def decode(psd, enc):                                                    # decode function
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        psd_c = psd[i % len(psd)]
        dec_c = chr((256 + ord(enc[i]) - ord(psd_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def Ent():                                                               # enter function
    print("Message = ", (Msg.get()))
    clear = Msg.get()
    p = psd.get()
    m = mode.get()
    if (m == 'd'):
        Result.set(decode(p, clear))
    else:
        Result.set(encode(p, clear))

def qExit():                                                             # exit function
    window.destroy()
  
def Reset():                                                             # reset function       
    Msg.set("")
    psd.set("")
    mode.set("")
    Result.set("")

# Reset button
#btnReset = 
Button(f1, padx = 8, pady = 4, bd = 10, fg = "black", 
                font = ('ROG Fonts', 16, 'bold'), width = 8, text = "RESET",
                 bg = "green", command = Reset).grid(row = 8, column = 1)

# Enter button
#btnEnter = 
Button(f1, padx = 8, pady = 4, bd = 10, fg = "black",
                font = ('ROG Fonts', 16, 'bold'), width = 10, text = "ENTER", 
                 bg = "powder blue", command = Ent).grid(row = 8, column = 2)

# Exit button
#btnExit = 
Button(f1, padx = 8, pady = 4, bd = 10, fg = "black", 
                font = ('ROG Fonts', 16, 'bold'), width = 8, text = "EXIT", 
                 bg = "red", command = qExit).grid(row = 8, column = 3)
  
window.mainloop()