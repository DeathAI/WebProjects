from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
# from dataBase import *
from remove import *
import manip as m
import os
from datetime import datetime
import calendar
import dates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


i=0
root = Tk()
root.geometry('2048x1024')
root.title("ATMOS Attendance Management and Operation Software LTD.")
root.config(bg="#003f88")
# canvas = Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
# canvas.pack()
# back1 = PhotoImage(file="back1.jpg")
# canvas.create_image(0,0,image=back1)

def open(btn=False):
    file = askopenfile(mode ='r', filetypes =[('Excel Files', '*.xlsx')])
    return file.name
    # if btn:
    #     btn = Button(root, text ='Open', command = lambda:open_file())
    #     btn.pack(side = TOP, pady = 10)
    # else:
    #     open_file()

def button(name1,txt,x,y,func,w=5,back="white",font1=("montserrat bold",12),fore="black"):
    global submit
    submit = Button(root,name=name1,text=txt,command=func,borderwidth=0,width=w,bg=back,font=font1,fg=fore)
    submit.configure()
    submit.pack()
    submit.place(relx=x,rely=y,anchor="center")
    return submit

sel = 'hello'
def callback(category):
    print(category)
    global sel
    if category == 'College':
        sel="col"
        global click
        click = StringVar()
        click.set( "Select Sem" )
        global college
        college = ttk.OptionMenu(root,click,"Select Sem",*options_college,command=loader)
        college.config(width=10 )
        college.place(relx=0.113,rely=0.146,anchor="center")
        # button("sub","Submit",0.7,0.8,func=loader,w=8)
    elif category.replace(' ','') == 'School':
        print("in")
        sel="sch"
        global ck
        ck = StringVar()
        ck.set('Select class')
        global school
        school = ttk.OptionMenu(root,ck,"Select Class",*options_school,command=loader)
        school.place(relx=0.113,rely=0.146,anchor="center")
        # button("sub","Submit",0.7,0.8,loader,w=6)
    else:
        pass
        # button("sub","Submit",0.7,0.8,loader,w=6)
    
menubar = Menu(root)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New Record', command = None)
file.add_command(label ='Open...', command = open)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Add', command = None)
edit.add_command(label ='Remove', command = None)

edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='ATMOS Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About ATMOS', command = None)

root.config(menu = menubar)

logo=PhotoImage(file="ATMOS LOGO.png")
root.iconphoto(False,logo)

options_cate = [
    "College",
    "School",
    "Staff"
]

options_school = [
    "Class 1",
    "Class 2",
    "Class 3",
    "Class 4",
    "Class 5",
    "Class 6",
    "Class 7",
    "Class 8",
    "Class 9",
    "Class 10",
    "Class 11",
    "Class 12"
]

options_college=[
    "Sem 1",
    "Sem 2",
    "Sem 3",
    "Sem 4",
    "Sem 5",
    "Sem 6"
]

select_out = ""
select_in = ""

def clr_scr():
    
    global select_out, select_in
    if sel == "sch":
        select_out = "School"
        select_in = ck.get()
        school.destroy()
    elif sel == "col":
        select_out = "College"
        select_in = click.get()
        college.destroy()
    elif sel == "staff":
        select_out = "Staff"
    
    temp.destroy()
    for i in range(1,4):
        btn = root.nametowidget(f"btn{i}")
        btn.destroy()
    
def clr_scr_2():
    tree.destroy()
    submit.destroy()
    label1.destroy()
    title2.destroy()
    title3.destroy()
    for i in range(1,10):
        btn = root.nametowidget(f"btn{i}")
        btn.destroy()
    
# def back():
#     frame = Frame(root,highlightthickness=0,bd=0,background="#003f88")
#     image=Image.open("ATMOS LOGO half.png")
#     i=image.resize((500,600))
#     img = ImageTk.PhotoImage(i)
#     label = Label(frame, image = img,bg="#003f88",highlightthickness=0,bd=0,border=-1,pady=0)
#     label.place(relx=0.05,rely=0.15)
#     clr_scr_2()
#     temp=main()
#     temp.pack(fill="both", expand=True)


names = []
ids = []
att = []
date = []

def attendance():
    global path,month,date
    month = calendar.month_name[datetime.now().month]
    
    d=datetime.now().day
    m=datetime.now().month
    y=datetime.now().year

    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
    
    if len(date)==0:
        date=[d,m,y]

    excel_data(path,att,date)
    messagebox.showinfo("Attention", "Your Data has been Saved!!")

def save():
    global path,month
    month = calendar.month_name[datetime.now().month]
    d=datetime.now().day
    m=datetime.now().month
    y=datetime.now().year 
    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
    dates = [d,m,y]
    print(path)
    if os.path.isfile(path+".xlsx"):
        pass
    else:
        excelbody(path,m,y,names,ids)
    messagebox.showinfo("Attention", "Your Data has been Saved!!")

def loader(selection):
    
    global select_in,select_out
    select_in=selection
    if sel == "sch":
        select_out = "School"
        
    elif sel == "col":
        select_out = "College"
        
    elif sel == "staff":
        select_out = "Staff"
    month = calendar.month_name[datetime.now().month]
    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year) 

    if os.path.isfile(path+".xlsx"):
        create_list()
        remove_all(False)
        import_excel(path,window=False)
    else:
        remove_all(False)
        
def next_page(cate="school"):
    clr_scr()
    print(cate)
    callback(cate)
    global tree,title2
    title2 = Label(text="Attendance",font=('montserrat semibold',30),bg="#003f88",fore="white")
    title2.place(relx=0.16,rely=0.09,anchor="center")
    img1= Image.open("ATMOS LOGO.png")
    img2=img1.resize((50,60))
    img3=ImageTk.PhotoImage(img2)
    global label1
    label1 = Label(image = img3,bg="#003f88",highlightthickness=0,bd=0,border=-1,pady=0)
    label1.place(relx=0.025,rely=0.05,anchor="center")

    style = ttk.Style() 
    style.theme_use('alt')
    style.configure("Treeview",font=('montserrat semibold',11))
    
    tree = ttk.Treeview(root, column=("Name", "ID", "Attendance"), show='headings', height=25)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Attendance")
    tree.place(relx=0.08,rely=0.17)
    month = calendar.month_name[datetime.now().month]
    
    button("btn1","Import Excel...",0.2,0.84,import_excel,12,back="#ffd500")
    button("btn2","Generate Report...",0.283,0.84,report,14,back="#ffd500")
    button("btn3","Add Student",0.258,0.145,add,14,back="#ffd500")
    button("btn4","Remove Student",0.348,0.145,rem,14,back="#ffd500")
    button("btn5","Edit Data",0.18,0.145,edit_tree,10,back="#ffd500")
    button("btn8","Remove All",0.123,0.84,remove_all,12,back="#ffd500")
    global title3
    
    title3 = Label(text="Select a record and select Present/Absent",font=('montserrat semibold',12),bg="#003f88",fore="white")
    title3.place(relx=0.75,rely=0.19,anchor="center")
    button("btn9","Present",0.7,0.23,present,12,back="#32cd32",font1=("montserrat semibold",12),fore="white")
    button("btn10","Absent",0.8,0.23,absent,12,back="#FF3939",font1=("montserrat semibold",12),fore="white")
    button("btn11","Save Attendance",0.373,0.84,attendance,14,back="#ffd500")
    button("btn12","Present All",0.7,0.3,present_all,12,back="#32fd32",font1=("montserrat semibold",12),fore="white")
    button("btn13","Absent All",0.8,0.3,absent_all,12,back="red",font1=("montserrat semibold",12),fore="white")
    button("btn14","Generate Pie Chart",0.8,0.8,pie,12,back="red",font1=("montserrat semibold",16),fore="white")

    clk = StringVar()
    clk.set( "Select Sem" )
    options_date=dates.getDates(dates.month,dates.year)
    print(options_date)
    global date
    cur_date=str(dates.getCurDate()).replace(",","/")[1:-1]
    date = ttk.OptionMenu(root,clk,f"{cur_date}",*options_date,command=past_data)
    date.config(width=14)
    date.place(relx=0.435,rely=0.146,anchor="center")
    
def past_data(selection):
    print(selection)
    create_list()
    global date
    month = calendar.month_name[datetime.now().month]
    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
    date=[selection,dates.month,dates.year]
    print(date)
    list=m.pastDataExcel(path,[selection,dates.month,dates.year])
    print(list)
    item=1
    for i in range(0,len(list)):
        global name,id
        name=names[i]
        id=ids[i]
        cur_item="I00"+str(item)
        if str(list[i]).lower()=="true":
            tree.item(cur_item, text="blub",image=img, values=(id,name,"Present"))
        elif str(list[i]).lower()=="false":
            tree.item(cur_item, text="blub",image=img, values=(id,name,"Absent"))
        else:
            tree.item(cur_item, text="blub",image=img, values=(id,name))
        item+=1
    
def pie():
    create_list()
    sel = select_Item()
    name = sel['values'][0]
    id=sel['values'][0]
    root = Tk()
    frameChartsLT = Frame(root)
    frameChartsLT.pack()
    month = calendar.month_name[datetime.now().month]
    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+'.xlsx'
    # data=read_DB(filename=path)
    data=m.rg(path)
    i=ids.index(id)
    a=data[i+1][-1]

    stockSplitExp = [a,100-a]

    fig = Figure() # create a figure object
    ax = fig.add_subplot(111) # add an Axes to the figure

    ax.pie(stockSplitExp, radius=1,autopct='%0.2f%%', shadow=True,)

    chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
    chart1.get_tk_widget().pack()

    root.mainloop()

def present_all():
    create_list()
    item=1
    for i in range(0,len(names)):
        cur_item="I00"+str(item)
        global name,id
        print(names)
        print(ids)
        name=names[i]
        id=ids[i]
        try:
            att[i]="True"
        except:
            att.insert(i,"True")
        item+=1
        tree.item(cur_item, text="blub",image=img  , values=(id,name,"Present"))

def absent_all():
    item=1
    for i in range(0,len(names)):
        cur_item="I00"+str(item)
        global name,id
        name=names[i]
        id=ids[i]
        try:
            att[i]="false"
        except:
            att.insert(i,"false")
        item+=1
        tree.item(cur_item, text="blub",image=img  , values=(id,name,"Absent"))

def create_list():
    month = calendar.month_name[datetime.now().month]
    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)
    data=read_DB(filename=path)
    global names,ids
    names=data[1]
    ids=data[0]
    print(names)
    print(ids)
    
def present():
    global names,ids
    selected_item = tree.selection()[0]
    print(selected_item)
    sel = select_Item()
    name = sel['values'][1]
    id2 = sel['values'][0]
    i=0
    while i<=len(names)-1:
        global att
        print("names:",names)
        print(i)
        if names[i] == name:
            names[i]=name
            ids[i]=id2
            try:
                att[i]="True"
            except:
                att.insert(i,"True")
            break
        i+=1
    image=Image.open("present.png")
    img = ImageTk.PhotoImage(image)
    tree.item(selected_item, text="blub",image=img  , values=(id2,name,"Present"))
    
def absent():
    global names,ids
    selected_item = tree.selection()[0]
    sel = select_Item()
    name = sel['values'][1]
    id2 = sel['values'][0]
    i=0
    while i<=len(names):
        global att
        if names[i] == name:
            names[i]=name
            ids[i]=id2
            try:
                att[i]="False"
            except:
                att.insert(i,"False")
            break
        i+=1
    image=Image.open("present.png")
    i=image.resize((20,10))
    img = ImageTk.PhotoImage(i)
    tree.item(selected_item, text="blub",image=img, values=(id2,name,"Absent"))

def remove_all(check=True):
    global names,ids
    if check:
        try:
            i=len(names)-1
            while i>=0:
                names.pop(i)
                ids.pop(i)
                i-=1
            for item in tree.get_children():
                tree.delete(item)
        except:
            messagebox.showerror("Warning!", "Please add data and save before removing data!")
        month = calendar.month_name[datetime.now().month]
        path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
        cls(path)
        excelbody(path,dates.month,dates.year,[],[])
    else:
        j=len(names)-1
        while j>=0:
            names.pop(j)
            ids.pop(j)
            j-=1
        for item in tree.get_children():
            tree.delete(item)   
    
def add():
    my_w=Tk()
    
    my_w.title("ATMOS")
    l0 = Label(my_w,  text='Add Student',
                font=('Helvetica', 16), width=30)  
    l0.grid(row=2,column=1,columnspan=4) 

    l1 = Label(my_w,  text='Name: ', width=10 )  
    l1.grid(row=3,column=1,columnspan=2) 

    # add one text box
    t1 = Text(my_w,  height=1, width=10,bg='white') 
    t1.grid(row=3,column=2,columnspan=2) 

    l2 = Label(my_w,  text='ID: ', width=10,)  
    l2.grid(row=4,column=1,columnspan=2) 

    # add one text box
    t2 = Text(my_w,  height=1, width=4,bg='white') 
    t2.grid(row=4,column=2,columnspan=2)


    my_str = StringVar()
    l5 = Label(my_w,  textvariable=my_str, width=10 )  
    l5.grid(row=8,column=1)
    
    b1 = Button(my_w,  text='Add Record', width=10, 
               command=lambda: add_data(),back="#ffd500")  
    b1.grid(row=6,column=2,columnspan=2,rowspan=2) 
    
    def add_data():
        global tree
        my_name=str(t1.get("1.0",END)) # read name
        my_id=int(t2.get("1.0",END))
        my_name.replace(' ','')
        my_name.replace('\n','')
        print("names = ",my_name)
        print("id = ",my_id)
        
        month = calendar.month_name[datetime.now().month]
        path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
        print(os.path.isfile(path))
        print("flag=",names,ids)
        names.append(my_name)
        ids.append(my_id)
        if not(os.path.isfile(path)):
            excelbody(path,dates.month,dates.year,names,ids)
        m.add_xl(path,int(my_id),my_name)
    
        tree.insert("",'end',values=(my_id,my_name))
        print("flag 4")
        t1.delete('1.0',END)  # reset the text entry box
        t2.delete('1.0',END)  # reset the text entry box
        print("flag 5")
        my_str.set("Data added ")
        t1.focus()   
        # l5.after(3000, lambda: my_str.set('') )
    my_w.mainloop()

def rem():
    try:
        month = calendar.month_name[datetime.now().month]
        path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
        sel = select_Item()
        cur = sel['values'][0]
        print(cur)
        del_row(path,cur)
    except:
             messagebox.showerror("Warning!", "Please select the data to be Removed!")
    selected_item = tree.selection()[0]
    tree.delete(selected_item)

def select_Item():
    cur_item = tree.focus()
    return tree.item(cur_item)

def edit_tree():
    
    my_w=Tk()
    my_w.title("ATMOS")
    l0 = Label(my_w,  text='Edit Student Details',
                    font=('Helvetica', 16), width=30)  
    l0.grid(row=2,column=1,columnspan=4) 

    l1 = Label(my_w,  text='Name: ', width=10 )  
    l1.grid(row=3,column=1,columnspan=2) 

        # add one text box
    t1 = Text(my_w,  height=1, width=10,bg='white') 
    t1.grid(row=3,column=2,columnspan=2) 

    l2 = Label(my_w,  text='ID: ', width=10,)  
    l2.grid(row=4,column=1,columnspan=2) 

        # add one text box
    t2 = Text(my_w,  height=1, width=4,bg='white') 
    t2.grid(row=4,column=2,columnspan=2)
    
    b1 = Button(my_w,  text='Edit Record', width=10, 
            command=lambda: edit_data(),back="#ffd500")  
    b1.grid(row=6,column=2,columnspan=2,rowspan=2) 
    
    def edit_data():
        try:
            name = t1.get("1.0",END)
            name.replace(' ','')
            name.replace('\n','')
            id2 = int(t2.get("1.0",END))
            i=0
            global names,ids
            selected_item = tree.selection()[0]
            sel = select_Item()
            cur = sel['values'][0]
            month = calendar.month_name[datetime.now().month]
            path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
            while i<len(names):
                print(ids[i],cur)
                if ids[i] == cur:
                    print("in")
                    print(path,ids[i],id2,names[i],name)
                    m.edit_xl(path,ids[i],id2,names[i],name)
                i+=1
            tree.item(selected_item, text="blub", values=(id2,name))
            t1.delete('1.0',END) 
            t2.delete('1.0',END)
        except:
            messagebox.showerror("Warning!", "Please select an existing record to edit data!")
            return
        
    my_w.mainloop()

def report():
    month = calendar.month_name[datetime.now().month]
    path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
    # filename=open()
    # m.reportGroup(path,filename,dates.month,dates.year)
    import genrate as gen
    gen.main(path)

def import_excel(path1="demo",window=True):
    global names,ids
    if window:
        file_name=open()
        file_name=file_name.replace(".xlsx","")
        data=m.read_DB(filename=file_name)

        names1=data[1]
        ids1=data[0]
        month = calendar.month_name[datetime.now().month]
        path="data" + "\\" + select_out + "\\" + select_in + "\\" + month + str(datetime.now().year)+".xlsx"
        if not os.path.isfile(path):
            excelbody(path,dates.month,dates.year,names1,ids1)
        else:
            for i in range(0,len(names1)):
                m.add_xl(path,ids1[i],names1[i])
                try:
                    names[i]=names1[i]
                    ids[i]=ids1[i]
                except:
                    names.append(names1[i])
                    ids.append(ids1[i])
        i=0
        while(i!=len(names)):
        
            tree.insert("",'end',values=(ids[i],names[i]))
            i+=1

    else:
        print(path1)
        data=m.read_DB(filename=path1)
        print(data)
        names2=data[1]
        ids2=data[0]
        if not os.path.isfile(path1+'.xlsx'):
            excelbody(path1,dates.month,dates.year,names,ids)
   
        i=0
        while(i!=len(names2)):
        
            tree.insert("",'end',values=(ids2[i],names2[i]))
            i+=1
    
frame = Frame(root,highlightthickness=0,bd=0,background="#003f88")
image=Image.open("ATMOS LOGO half.png")
i=image.resize((500,600))
img = ImageTk.PhotoImage(i)
label = Label(frame, image = img,bg="#003f88",highlightthickness=0,bd=0,border=-1,pady=0)
label.place(relx=0.05,rely=0.15)
    
def main():
    global frame,img,label
    frame = Frame(root,highlightthickness=0,bd=0,background="#003f88")
    image=Image.open("ATMOS LOGO half.png")
    i=image.resize((500,600))
    img = ImageTk.PhotoImage(i)
    label = Label(frame, image = img,bg="#003f88",highlightthickness=0,bd=0,border=-1,pady=0)
    label.place(relx=0.05,rely=0.15)
   
    title = Label(frame,text="Welcome to ATMOS...",font=('montserrat semibold',45),bg="#003f88",fore="white")
    title.place(relx=0.6,rely=0.2,anchor="center")
    
    title1 = Label(frame,text="Select your Institution:",font=('montserrat semibold',15),bg="#003f88",fore="white")
    title1.place(relx=0.48,rely=0.3,anchor="center")


    # label2 = Label(frame, text=" 🏫 ",bg="#003f88",highlightthickness=0,bd=0,border=-1,pady=0, font=('montserrat semibold',45))
    # label2.place(relx=0.5,rely=0.5)

    button("btn1","School",0.45,0.5,func  = lambda m="School ":next_page(m),w=12,back="#ffd500")
    button("btn2","College",0.55,0.5,func = lambda m="College":next_page(m),w=12,back="#ffd500")
    button("btn3","Staff",0.65,0.5,func = lambda m="Staff":next_page(m),w=12,back="#ffd500")
    
    return frame

temp=main()
temp.pack(fill="both", expand=True)

root.mainloop()