import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk


if __name__ == '__main__':

    window = tk.Tk()
    window.geometry('1000x800')

    frame1 = tk.Frame(window, width=200, height=400, relief='solid')
    frame2 = tk.Frame(window, width=600, height=400, padx=20, pady= 20, relief='solid')
    frame3 = tk.Frame(window, width=1000, height= 100, relief='solid')
    frame4 = tk.Frame(window, width=1000, height= 300, relief='solid')

    tree = ttk.Treeview(frame1, show='tree')
    item = tree.insert("", tk.END, text='DB')
    subitem1 = tree.insert(item, tk.END, text='TABLE1')
    subitem2 = tree.insert(item, tk.END, text='TABLE2')
    subitem3 = tree.insert(item, tk.END, text='TABLE3')
    tree.pack()
    
    tree2 = ttk.Treeview(frame2, show='headings')

    b1 = tk.Button(frame3, text='기능1')
    b2 = tk.Button(frame3, text='기능2')
    b3 = tk.Button(frame3, text='기능3')
    b4 = tk.Button(frame3, text='기능4')
    b5 = tk.Button(frame3, text='기능5')

    b1.grid(row=0, column=0, padx= 20)
    b2.grid(row=0, column=1, padx= 20)
    b3.grid(row=0, column=2, padx= 20)
    b4.grid(row=0, column=3, padx= 20)
    b5.grid(row=0, column=4, padx= 20)

    frame1.grid(row=0, column=0)
    frame2.grid(row=0,column=1)
    frame3.grid(row=1, column=0)
    frame4.grid(row=2, column=0)

    


    #treeview = ttk.Treeview()


    window.mainloop()
