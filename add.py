from tkinter import *
import csv

def add_contacts():

    app = Tk()
    app.geometry('500x400')
    app.resizable(0,0)
    app.title("Ywu : Add ")
    app.config(bg="#424242")

    global nam
    global ph
    global add
    nam = StringVar()
    ph = StringVar()
    add = StringVar()

    Label(app, text="ADD CONTACTS\n", font="arial 25 bold",bg="#424242",  fg = "#00FFFF").pack()
    Label(app,text=" Name ", font="arial 20 normal",bg="#424242",  fg = "#7FFFD4").place(x=190,y=75)
    Entry(app,textvariable=nam).place(x=175,y=120,height=40)
    Label(app,text="Phone Number ", font="arial 20 normal",bg="#424242",  fg = "#7FFFD4").place(x=145,y=150)
    Entry(app,textvariable=ph).place(x=175,y=195,height=30)
    Label(app,text=" Address ", font="arial 20 normal",bg="#424242",  fg = "#7FFFD4").place(x=175,y=240)
    Entry(app,textvariable=add).place(x=175,y=285,height=30)


    Button(app,text="ADD",font="arial 15 bold",command=write_it,bg="red",padx=20, pady=15).place(x=190,y=330)

    app.mainloop()

def write_it():
    
    your_name = nam.get()
    your_ph_no = ph.get()
    your_address = add.get()
    print(f"{your_name},{your_ph_no},{your_address}")

    with open("contacts.csv","a") as file:
        # file.write("\n")
        # file.write(f"{your_name},{your_ph_no},{your_address}")
        writer = csv.DictWriter(file,fieldnames=["name","ph_no","add"])
        writer.writerow({"name":your_name, "ph_no":your_ph_no, "add":your_address})
        
   
def finish():
    return exit()


add_contacts()


