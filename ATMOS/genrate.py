from tkinter import ttk
from tkinter import *
from manip import *
# from pandas import *
from dates import *
def main(path):
    root=Tk() 
    root.geometry('2040x1020')
    root.title("student Report")
    root.config(bg="#9cc")
    # Using treeview widget
    game_farame=Frame(root,width=1900,height=800)
    game_farame.pack()
    #scrollbar
    scroll=Scrollbar(game_farame)
    scroll.pack(side=RIGHT,fill=Y)
    scroll=Scrollbar(game_farame,orient='horizontal')
    scroll.pack(side=BOTTOM,fill=X)
    # tv=ttk.Treeview(game_farame,yscrollcommand=scroll.set,xscrollcommand=scroll.set)
    tv = ttk.Treeview(game_farame,yscrollcommand=scroll.set,xscrollcommand=scroll.set,columns=(1,2,3),height=80)
    tv.pack()
    selected=tv.focus()
    scroll.config(command=tv.yview)
    scroll.config(command=tv.xview)
    a=[f'{i}-{month}-{year}' for i in getDates(month,year)]
    tv['columns']=('id', 'Name', *a , 'Persentage')
    # tv['rows']=('Dates')

    tv.column('#0', width=0, stretch=NO)
    tv.column('id', anchor=CENTER, width=100,)
    tv.column('Name', anchor=CENTER, width=80)
    for i in a:
        tv.column(i,anchor=CENTER, width=70)
    tv.column('Persentage', anchor=CENTER, width=80)
    # tv.row('Dates', anchor=CENTER, width=80)
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('id', text='id', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    for i in a:
        tv.heading(i,text=str(i),anchor=CENTER)
    tv.heading('Persentage', text='Persentage', anchor=CENTER)
    tv.insert("",'end',values=())
    data = rg(path)
    print(data)
    data.pop(0)
    data1=[]
    for x in data:
        list1=[x[0],x[1]]
        for y in x[2:-1]:
            att="Absent"
            if y==True:
                att="Present"
            list1.append(att)
        list1.append(x[-1])
        tv.insert("",'end',values=list1)
        data1.append(list1)


    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    tv.pack(pady=100,padx=50)
    root.mainloop()

    def genrateexcel():
        pass

    def report(l1):
        global per,total,count,name,identity
        count=0
        for item in l1:
            if item.lower()=="true":
                count+=1
        total=len(l1)
        per= count/total*100
        per=f"{per}%"
        
    report(["true","true","false","false"])
    def download():
        global FileExistsError

# main("data/College/Sem 2/March2023.xlsx")