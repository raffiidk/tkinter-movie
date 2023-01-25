from tkinter import *
from PIL import ImageTk, Image

def showSelect():
    sList = listWin.get(listWin.curselection())
    print(type(sList))
    return sList

def openWin():
    #Open NEW window with movie
    app2 = Tk()
    app2.title("Movie player")
    frame = LabelFrame(app2,padx=15,pady=15)
    frame.grid(row=0,column=0)
    img = ImageTk.PhotoImage(Image.open("image.jpg"))
    labelN = Label(frame, image = img)
    labelN.pack()
    return


app = Tk()
app.title("lean")
frame1 = LabelFrame(app, text="Movies",padx=15, pady=15)
frame1.grid(row=0, column=0)



listWin = Listbox(master=frame1,selectmode=BROWSE,)
listWin.insert(0,"Movie 1")
listWin.insert(1,"Movie 2")
listWin.insert(2,"Movie 3")
listWin.pack()

option = Label(master=frame1,textvariable="You selected: {}".format(showSelect()))
#Label that will display name of movie 

frame2 = LabelFrame(app, text="Open movie", padx=15, pady=15)
frame2.grid(row=0, column=1)
open = Button(frame2, text="Select",command=openWin())
open.pack()

#On select, display new window/ do something

app.mainloop()
