
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import threading
import sqlite3
import time
import os
from tkinter.font import BOLD


root = Tk()
root.geometry('1000x500')



def openFile(filename):
    os.system('python '+filename)

#! First Page Buttons

#? Add Order
addOrder = Button(root, text='Add A New Order', font=('Arial', 13, BOLD), pady=0, padx=20, borderwidth=2, bg='#f05454', fg='white', command= lambda: openFile('order.py') )
addOrder.pack(pady=(100,0))
#? Manage Foods
manageFood = Button(root, text='Manage Foods', font=('Arial', 13, BOLD), pady=0, padx=30, borderwidth=2, bg='#f05454', fg='white', command= lambda: openFile('foods.py'))
manageFood.pack(pady=(30,0))
#? Manage Customers
manageCustomer = Button(root, text='Manage Customers', font=('Arial', 13, BOLD), pady=0, padx=12, borderwidth=2, bg='#f05454', fg='white', command= lambda: openFile('customers.py'))
manageCustomer.pack(pady=(30,0))
#? Exit
exit = Button(root, text='Exit', font=('Arial', 13, BOLD), pady=0, padx=75, borderwidth=2, bg='#f05454', fg='white', command=root.destroy)
exit.pack(pady=(30,0))


root.mainloop()
