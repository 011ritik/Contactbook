# python phonebook

from tkinter import *
from add import *
from add import finish
from view import view_contacts
from delete import *

window = Tk()
window.geometry("500x420")
window.title("Ywu : PhoneBook")
window.resizable(0,0)
window.config(bg = "#424242")

# Creating a menu 

Label(window, text = "-PhoneBook-\n",font="arial 30 bold", bg="#424242", fg = "#00FFFF").pack()
Button(window, text="1. ADD CONTACTS", font ="arial 15 normal", bg ="#424242", fg="#7FFFD4", command= add_contacts).pack()   #add comannd in the button to open a new window
Label(window,text="",bg="#424242").pack()
Button(window, text="2. VIEW CONTACTS", font ="arial 15 normal", bg ="#424242", fg="#7FFFD4", command = view_contacts).pack()
Label(window,text="",bg="#424242").pack()
Button(window, text="3. DELETE CONTACTS", font ="arial 15 normal", bg ="#424242", fg="#7FFFD4",command=delete_contacts).pack()
Label(window,text="",bg="#424242").pack()
Button(window, text="4. EXIT", font ="arial 15 normal", bg ="#424242", fg="#7FFFD4",command=finish).pack()

window.mainloop()

