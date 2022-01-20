from time import monotonic
from tkinter import *

#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x500")

#Providing title to the form
root.title('🪐Planetary weight calculator')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 = Label(root,text="🪐Planetary weight calculator", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=80,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 = Label(root,text="Enter your weight on earth🌏:", width=20,font=("bold",15))
label_1.place(x=100,y=100)

earth_weight = StringVar(root)
#this will accept the input string text from the user.
entry_1=Entry(root, textvariable=earth_weight)
entry_1.place(x=110,y=130)

#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()

#the variable 'var2' mentioned here holds Integer Value, by default 0
var2=IntVar()

mars = Label(root,text="", width=20,font=("bold",15))
mars.place(x=100,y=200)
moon = Label(root,text="", width=20,font=("bold",15))
moon.place(x=100,y=230)
jupiter = Label(root,text="", width=20,font=("bold",15))
jupiter.place(x=100,y=260)
mercury = Label(root,text="", width=20,font=("bold",15))
mercury.place(x=100,y=290)
venus = Label(root,text="", width=20,font=("bold",15))
venus.place(x=100,y=320)
saturn = Label(root,text="", width=20,font=("bold",15))
saturn.place(x=100,y=350)
uranus = Label(root,text="", width=20,font=("bold",15))
uranus.place(x=100,y=380)
neptune = Label(root,text="", width=20,font=("bold",15))
neptune.place(x=100,y=410)

def onclick():
  earth_weight_float = float(earth_weight.get())
  mars["text"] = "Weight on Mars: {} kg".format(round(earth_weight_float*3.7/9.8, 2))
  moon["text"] = "Weight on Moon: {} kg".format(round(earth_weight_float*1.62/9.8, 2))
  jupiter["text"] = "Weight on Jupiter: {} kg".format(round(earth_weight_float*24.79/9.8, 2))
  mercury["text"] = "Weight on Mercury: {} kg".format(round(earth_weight_float*3.7/9.8, 2))
  venus["text"] = "Weight on Venus: {} kg".format(round(earth_weight_float*8.87/9.8, 2))
  saturn["text"] = "Weight on Saturn: {} kg".format(round(earth_weight_float*10.74/9.8, 2))
  uranus["text"] = "Weight on Uranus: {} kg".format(round(earth_weight_float*8.87/9.8, 2))
  neptune["text"] = "Weight on Neptune: {} kg".format(round(earth_weight_float*11.15/9.8, 2))


#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="black",fg='black',command=onclick).place(x=100,y=160)


#this will run the mainloop.
root.mainloop()
