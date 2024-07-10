import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

def func_1():
    subwindow = tk.Toplevel()
    subwindow.geometry('400x400')
    


if __name__ == '__main__':
    
    window = tk.Tk()
    window.geometry('1000x800')

    tree_frame = tk.Frame(window)

    frame1 = tk.Frame(tree_frame, width=200, height=400, relief='solid')
    frame2 = tk.Frame(tree_frame, width=600, height=400, relief='solid')
    frame3 = tk.Frame(window, width=1000, height= 100, relief='solid')
    frame4 = tk.Frame(window, width=1000, height= 300, relief='solid')

    tree = ttk.Treeview(frame1, show='tree')
    item = tree.insert("", tk.END, text='DB')
    subitem1 = tree.insert(item, tk.END, text='TABLE1')
    subitem2 = tree.insert(item, tk.END, text='TABLE2')
    subitem3 = tree.insert(item, tk.END, text='TABLE3')
    tree.pack()
    
    tree2 = ttk.Treeview(frame2, columns=("Name", "Age", "City"), show='headings')
    
    tree2.heading("Name", text="col_1")
    tree2.heading("Age", text="col_2")
    tree2.heading("City", text="col_3")

    tree2.insert("", tk.END, values=("John Doe", 25, "New York"))
    tree2.insert("", tk.END, values=("Jane Smith", 30, "San Francisco"))
    tree2.insert("", tk.END, values=("Mike Johnson", 22, "Chicago"))
    tree2.pack()

    b1 = tk.Button(frame3, text='기능1', command=func_1)
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
    tree_frame.grid(row=0, column=0)
    frame3.grid(row=1, column=0)
    frame4.grid(row=2, column=0)

    


    #treeview = ttk.Treeview()


    window.mainloop()
