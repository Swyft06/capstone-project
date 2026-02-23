from tkinter import *
import speech_recognition as sr

root = Tk()
root.title("Task Manager")
root.geometry("400x450")

tasks = []

def updatelist():
    list.delete(0,END)
    for task in tasks:
        list.insert(END,task)

def addtask():
    task = entry.get()
    list.insert(END,task)
    entry.delete(0,END)
    

def deletetask():
    task = list.curselection()
    if task:
        list.delete(task)
        

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            status.config(text = 'Listening...')
            root.update()
            audio = r.listen(source)
        command = r.recognize_google(audio).lower()
        status.config(text = f"You said {command}")
        if 'add' in command:
            task = command.replace('add','').strip()
            if task != '':
                tasks.append(task)
                updatelist()
        elif 'delete' in command:
            task = command.replace('delete','').strip()
            if task in tasks:
                tasks.remove(task)
                updatelist()
            else:
                status.config(text = "Task not found")
        elif 'clear' in command:
            tasks.clear()
            updatelist()
    except:
        status.config(text = "Could not understand")

title = Label(root,text = "Task Manager",font = ('Arial',20))
title.pack(pady=10)

entry = Entry(root,width = 30)
entry.pack(pady=10)

add_button = Button(root,text = "Add task",command = addtask)
add_button.pack()

delete_button = Button(root,text = "Delete task",command = deletetask)
delete_button.pack()

voiceb = Button(root, text = "Say a command",command = listen)
voiceb.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

list = Listbox(root,width = 30,height = 12,yscrollcommand = scrollbar.set)
list.pack(pady = 20)

scrollbar.config(command = list.yview)

status = Label(root,text = "No voice detected")
status.pack()

root.mainloop()
