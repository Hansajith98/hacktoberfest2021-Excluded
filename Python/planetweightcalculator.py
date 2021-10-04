# Planet weight calculator by Facundo Pedaccio

#The program is capable of calculating the weight that the user enters on any planet in the solar system and some of its moons.
#We use the weight of the user on the earth (in KGf), which is equal to the mass of that body,
#to calculate gravity based on the formula
#Weight (in Newtons) = mass (in KG) * gravitational acceleration of the chosen planet (in m * s ^ 2).
#All this accompanied by a nice and nerdy user interface,
#which also includes some friendly reminders about physics. Like the meaning of weight and mass.


from tkinter import *



# User Interface (GUI)
ventana = Tk()
peso = IntVar()
planeta = StringVar()
res = StringVar()
ventana.geometry("1000x700")
ventana.title("How much would I weight in? APP")
ventana.iconbitmap("planet.ico")
gui = PhotoImage(file="gui.png")
guiplace = Label(ventana, image=gui)
guiplace.place(x=0, y=0, relwidth=1, relheight=1)


# Calculate weight function: based on W = m*g
# W = Weight, m = Mass, g = gravitational acceleration

def calcular():
    planetinput=str(planeta.get())
    mars = (peso.get()*3.7)//9.8
    moon = (peso.get()*(1.62))//9.8
    jupiter = (peso.get()*(24.79))//9.8
    saturno = (peso.get()*(10.74))//9.8
    mercury = (peso.get()*(3.70))//9.8
    venus = (peso.get()*(8.87))//9.8
    urano = (peso.get()*(8.87))//9.8
    neptune = (peso.get()*(11.15))//9.8
    Europa_moon = (peso.get()*(1.31))//9.8
    
    
    
    
# setting the result depending of the user planet input. I included a few exeption
#I included some exceptions with different ways of writing the same planet. Including Spanish and English languages
    
    if "Marte" in planetinput:
        res.set(str(mars )+ " KG")
    elif "marte" in planetinput:
        res.set(str(mars)+ " KG")
    elif "mars" in planetinput:
        res.set(str(mars)+ " KG")
    elif "Mars" in planetinput:
        res.set(str(mars)+ " KG")
    elif "MARS" in planetinput:
        res.set(str(mars)+ " KG")    
    elif "MARTE" in planetinput:
        res.set(str(mars)+ " KG")
    elif "Moon" in planetinput:
        res.set(str( moon)+ " KG")
    elif "MOON" in planetinput:
        res.set(str( moon)+ " KG")
    elif "LUNA" in planetinput:
        res.set(str( moon)+ " KG")    
    elif "Moon" in planetinput:
        res.set(str( moon)+ " KG")
    elif "Luna" in planetinput:
        res.set(str( moon)+ " KG")    
    elif "luna" in planetinput:
        res.set(str( moon)+ " KG")
    elif "moon" in planetinput:
        res.set(str( moon)+ " KG")
    elif "jupiter" in planetinput:
        res.set(str(jupiter)+ " KG")
    elif "Jupiter" in planetinput:
        res.set(str(jupiter)+ " KG")
    elif "JUPITER" in planetinput:
        res.set(str(jupiter)+ " KG")
    elif "Saturn" in planetinput:
        res.set(str(saturno)+ " KG")
    elif "Saturno" in planetinput:
        res.set(str(saturno)+ " KG")
    elif "SATURNO" in planetinput:
        res.set(str(saturno)+ " KG")
    elif "SATURN" in planetinput:
        res.set(str(saturno)+ " KG")
    elif "saturn" in planetinput:
        res.set(str(saturno)+ " KG")
    elif "saturno" in planetinput:
        res.set(str(saturno)+ " KG")
    elif "venus" in planetinput:
        res.set(str(venus)+ " KG")
    elif "Venus" in planetinput:
        res.set(str(venus)+ " KG")
    elif "VENUS" in planetinput:
        res.set(str(venus)+ " KG")
    elif "Mercury" in planetinput:
        res.set(str(mercury)+ " KG")
    elif "Mercurio" in planetinput:
        res.set(str(mercury)+ " KG")
    elif "mercury" in planetinput:
        res.set(str(mercury)+ " KG")
    elif "mercurio" in planetinput:
        res.set(str(mercury)+ " KG")
    elif "MERCURY" in planetinput:
        res.set(str(mercury)+ " KG")
    elif "MERCURIO" in planetinput:
        res.set(str(mercury)+ " KG")
    elif "Urano" in planetinput:
        res.set(str(urano)+ " KG")
    elif "urano" in planetinput:
        res.set(str(urano)+ " KG")
    elif "URANO" in planetinput:
        res.set(str(urano)+ " KG")
    elif "Uranus" in planetinput:
        res.set(str(urano)+ " KG")
    elif "uranus" in planetinput:
        res.set(str(urano)+ " KG")
    elif "URANUS" in planetinput:
        res.set(str(urano)+ " KG")
    elif "Neptuno" in planetinput:
        res.set(str(neptune)+ " KG")
    elif "neptuno" in planetinput:
        res.set(str(neptune)+ " KG")
    elif "NEPTUNO" in planetinput:
        res.set(str(neptune)+ " KG")
    elif "Neptune" in planetinput:
        res.set(str(neptune)+ " KG")
    elif "neptune" in planetinput:
        res.set(str(neptune)+ " KG")
    elif "NEPTUNE" in planetinput:
        res.set(str(neptune)+ " KG")
    elif "Europa" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    elif "europa" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    elif "EUROPA" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    elif "Europa moon" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    elif "EUROPA MOON" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    elif "europa moon" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    elif "Europa Moon" in planetinput:
        res.set(str(Europa_moon)+ " KG")
    
    else:
        res.set("Planet not found")
    
    
    
    
# Saving user inputs into variables. Peso = Weight, planeta = planet
peso = IntVar()
planeta = StringVar()

# Result variable
res = StringVar()



# Used fonts
fontentry= ("Montserrat", 15, "bold")
fontbuttom= ("Montserrat", 10, "bold")
fontresult = ("Montserrat", 20, "bold")


# Entry boxes
pesoentry = Entry(ventana, justify="center", font=(fontentry), bd=0,textvariable=peso)
pesoentry.place(x=285,y=253, width=370, height=37)

planeta = Entry(ventana,justify="center", font=(fontentry), bd=0,textvariable=planeta)
planeta.place(x=256,y=352,width=450, height=38)

# Result Label
textoR = Label(ventana,textvariable=res,font=(fontresult), bd=0, bg="alice blue", fg="black")
textoR.place(x=650,y=515)

# Calculate button
boton = Button(ventana,text="Calculate",command=calcular,bg="white",fg="black", bd=0, font=(fontbuttom))
boton.place(x=433,y=453)
ventana.mainloop()
