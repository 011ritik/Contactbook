
from telnetlib import XASCII
from tkinter import *
import csv


lines = list()
def delete_contacts():

    app = Tk()
    app.geometry('500x400')
    app.resizable(0,0)
    app.title("Ywu : Delete ")
    app.config(bg="#424242")

    Label(app, text="Delete Contacts", font ="arial 30 bold", bg="#424242", fg = "#00FFFF").pack()

    Label(app,text="Enter the name to delete",font ="arial 20 bold", bg ="#424242", fg="#7FFFD4").place(x=100,y=100)
    global name
    name = StringVar()
    Entry(app,textvariable=name).place(x=200,y=150,height=30)

    Button(app,text="Delete",font="arial 20 bold",command=Delete,bg="red").place(x=200,y=200)

    app.mainloop()

def Delete():
    detail =str(name.get())
    with open("contacts.csv","r") as file:
        reader=csv.DictReader(file)
        for line in reader:
            lines.append(line)
            if detail == line["name"]:
                lines.remove(line)
            print(lines)
    with open("contacts.csv","w") as file:
        file.write("name,ph_no,add\n")
        writer = csv.DictWriter(file,fieldnames=["name","ph_no","add"])
        writer.writerows(lines)
