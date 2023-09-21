from tkinter import *
#joeditor
#By Erik "Joe" Pastori

root = Tk()
root.geometry("250x400")
joefont = ["Comic Sans MS", 20, "normal"]

icon = PhotoImage(file="Joeditor.png") 
root.iconphoto(False, icon)
root.title("Joeditor")

scroll=Scrollbar(root, orient='vertical')
scroll.pack(side=RIGHT, fill='y')

root.resizable(True,True)

joetuple = (joefont[0], joefont[1], joefont[2])

text = Text(root, yscrollcommand=scroll.set, font=joetuple)

scroll.config(command=text.yview)
text.pack()
root.mainloop()