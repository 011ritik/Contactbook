from tkinter import *
import csv

def view_contacts():

    app = Tk()
    app.geometry('500x400')
    app.resizable(1,1)
    app.title("Ywu : View")
    app.config(bg="#424242")

    #Giving the size of the column and number of the column
    app.columnconfigure(index=0, weight=133)
    app.columnconfigure(index=1, weight=133)
    app.columnconfigure(index=2, weight=133)
    
    #title 
    Label(app, text="View Contacts", font="arial 25 bold",bg='#424242',fg = "#00FFFF").grid(row=0,column=1)

    #Headers of phonebook
    Label(app,text="Name", font="arial 20 normal",bg='#424242',fg="#7FFFD4").grid(row=1,column=0)
    Label(app,text="Ph-No", font="arial 20 normal",bg='#424242',fg="#7FFFD4").grid(row=1,column=1)
    Label(app,text="Address", font="arial 20 normal",bg='#424242',fg="#7FFFD4").grid(row=1,column=2)

    #Reading form the file and printing it in the GUI
    with open("contacts.csv","r") as file:
        i=1
        reader = csv.DictReader(file)
        # for line in sorted(file):
        #     j=0
        #     i += 1
        #     j += 1
        #     n= line.split(",")
        #     print(n)
        #     name,ph,add = line.rstrip().split(",")
        #     print(f"{name} , {ph} , {add}")
          
        #     Label(app, text=name, font= "arial 15 normal",bg='#424242').grid(row=i,column=0)
        #     Label(app, text=ph, font= "arial 15 normal",bg='#424242').grid(row=i,column=j)
        #     Label(app, text=add, font= "arial 15 normal",bg='#424242').grid(row=i,column=j+j)
        for row in reader:
            j=0
            i += 1
            j += 1
            
            Label(app, text=row["name"], font= "arial 15 normal",bg='#424242',fg="#EE0000").grid(row=i,column=0)
            Label(app, text=row["ph_no"], font= "arial 15 normal",bg='#424242',fg="#EE0000").grid(row=i,column=j)
            Label(app, text=row["add"], font= "arial 15 normal",bg='#424242',fg="#EE0000").grid(row=i,column=j+j)
            
    app.mainloop()

