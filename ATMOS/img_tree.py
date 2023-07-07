from tkinter import ttk
import tkinter as tk
# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("380x380") 
my_w.title("www.plus2net.com")  
# Using treeview widget style 
style = ttk.Style()
style.configure('Treeview', rowheight=100)  # increase height 

trv = ttk.Treeview(my_w, selectmode ='browse',height=3)  
trv.grid(row=1,column=1,rowspan=5,padx=30,pady=20)
# number of columns
trv["columns"] = ("1")
# Defining heading
trv['show'] = 'tree headings'
#trv['show'] = 'tree'

trv.column("#0", width = 150, anchor ='center') # Width of column
trv.column("1", width = 130, anchor ='center')
# Headings  
# respective columns
trv.heading("#0", text ="#") # Text of the column 
trv.heading("1", text ="Name")


img1=tk.PhotoImage(file = "present.png")  # Path to 1 image 

img2=tk.PhotoImage(file = "Absent.png") 

trv.insert("",'end',iid='1',open=True,text='1',image=img1,values=('na-Alex'))
trv.insert("",'end',iid=2,open=True,text='2',image=img2,values=('n1-Alex'))

my_w.mainloop()