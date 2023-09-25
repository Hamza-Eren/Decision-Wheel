# -*- coding: utf-8 -*-
"""
@author: HamzaEren
"""

# Modules
from tkinter import Tk, ttk, Frame, Button, Entry, Label, Scrollbar, Text
from random import choice, randint

# Consts
LIST = []
NUMBER = 0
RESULT = ""
COUNT = 0

# Functions
def Active():
    w = notification_label.winfo_width()
    if w < 260:
        notification_label.place(width=w+1)
        app.after(2, Active)
    else:
        app.after(500, Inactive)

def Inactive():
    w = notification_label.winfo_width()
    if w > 1:
        notification_label.place(width=w-1)
        app.after(1, Inactive)
    else:
        notification_label.configure(background="#F0F0F0")

def Add(*args):
    word = word_entry.get()
    word_entry.delete(0, "end")
    if word in LIST:
        notification_label.config(text=f"{word} zaten listede..")
        notification_label.configure(background="orange")
    else:
        LIST.append(word)
        notification_label.config(text=f"{word} listeye eklendi..")
        notification_label.configure(background="green")
    Active()

def OpenList():
    global LIST
    
    list_app = Tk()
    list_app.title("Listedekiler")
    list_app.geometry("300x155")
    
    scroll = Scrollbar(list_app, orient='vertical')
    scroll.pack(side="right", fill='y')
    
    text = Text(list_app, yscrollcommand=scroll.set)
    
    for item in LIST:
        text.insert("end", item + "\n")
        
    scroll.config(command=text.yview)
    text.pack()

def DelList():
    LIST.clear()
    notification_label.config(text="Liste sıfırlandı.")
    notification_label.configure(background="red")
    Active()

def DetermineNumber(*args):
    global NUMBER
    NUMBER = randint(20, 30)
    wheel_frame.place(x=0, y=0, width=300, height=155)
    Spin()

def Spin():
    global RESULT, COUNT, NUMBER
    
    if len(LIST) != 0:
        choose = choice(LIST)
        if choose != RESULT:
            RESULT = choose
            result_label.config(text=RESULT)
            COUNT += 1
            
        if COUNT < NUMBER:
            app.after(100, Spin)
            
    else:
        result_label.config(text="Liste boş :(")
    
def BackToSetting(*args):
    wheel_frame.place_forget()
    setting_frame.place(x=0, y=0, width=300, height=155)

# App
app = Tk()
app.title("Decision Wheel")
app.geometry("300x155")
app.resizable(0, 0)

setting_frame = Frame(app)
setting_frame.place(x=0, y=0, width=300, height=155)
wheel_frame = Frame(app)
#wheel_frame.place(x=0, y=0, width=300, height=155)

notification_label = ttk.Label(setting_frame, text="", foreground="white")
notification_label.place(x=20, y=5, width=0, height=20)

word_entry = Entry(setting_frame)
word_entry.bind("<Return>", Add)
word_entry.bind("<space>", DetermineNumber)
word_entry.place(x=20, y=30, width=235, height=25)
word_entry.focus()
add_btn = Button(setting_frame, text="+", command=Add)
add_btn.place(x=255, y=30, width=25, height=25)

list_btn = Button(setting_frame, text="Listeyi görüntüle", command=OpenList)
list_btn.place(x=20, y=65, width=125, height=25)

del_btn = Button(setting_frame, text="Listeyi sıfırla", command=DelList)
del_btn.place(x=155, y=65, width=125, height=25)

decision_btn = Button(setting_frame, text="Çarkı çevir", command=DetermineNumber)
decision_btn.place(x=20, y=100, width=260, height=25)

close_wheel = Button(wheel_frame, text="𝐗", command=BackToSetting)
close_wheel.place(x=260, y=5, width=20, height=20)

sep1 = ttk.Separator(wheel_frame, orient='horizontal')
sep1.place(x=75, y=40, width=150, height=5)
sep2 = ttk.Separator(wheel_frame, orient='horizontal')
sep2.place(x=75, y=105, width=150, height=5)

result_label = Label(wheel_frame, text="", font="17")
result_label.place(x=75, y=45, width=150, height=60)

app.mainloop()