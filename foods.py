
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

foods = {'fish': 10000, # Toman
         'rice': 8000,
         'chips': 5000,
         'steak':30000,
         'meat': 25000,
         'noodles': 15000,
         'spagetti': 20000,
         'sushi': 22000
         }

foodsList = Listbox(root, height=10, width=20, font=('Mono', 12), borderwidth=5,relief="groove",  )
for item in foods:
    foodsList.insert(END, item)
foodsList.place(relx=0.12, rely=0.23, anchor='c')


#? Add Food

#? Delete Food
#? Exit


root.mainloop()
