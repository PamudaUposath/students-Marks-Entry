#!/usr/bin/python

import tkinter as tk
from tkinter import scrolledtext
import sys
import pathlib

PROGRAM_NAME = "students-Marks-Entry"
VERSION = 'v1.0.0'

n = []    # NOTE = this is a list of tuples in the from of (subject of type str, marks of that subject in type float)

root = tk.Tk()
root.title(PROGRAM_NAME + " - " + VERSION)
canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()
root.protocol('WM_DELETE_WINDOW', lambda:sys.exit(0))

# window to ask studen's name
root.withdraw()
nameWin = tk.Toplevel()
nameWin.title(PROGRAM_NAME + " - " + VERSION)
nameWin.geometry('400x150')
nameInLabel = tk.Label(nameWin, text="Enter student's name below", pady=10)
nameInLabel.place(anchor='n', relx=0.5)
nameInEntry = tk.Entry(nameWin)
nameInEntry.place(anchor='c', width=380, height=40, y=50, relx=0.5)
p = "empty"
def setStudName(name):
    if name != "":
        global p
        p = name
        root.title(p)
        root.deiconify()
        nameWin.destroy()
nameInBtn = tk.Button(nameWin, text="Submit", command=lambda:setStudName(nameInEntry.get()))
nameInBtn.place(anchor="c", relx=0.5, y=120, width=100, height=50)
nameWin.protocol('WM_DELETE_WINDOW', lambda:sys.exit(0))

subjectsBoard = scrolledtext.ScrolledText(root, font=("Liberation Serief", 12))

_Minimum_ = None
_Maximum_ = None
_Total_ = None
_Avarage_ = None

def Maximum():
    a = n
    Max=a[0][1]
    for i in range(1,len(a)):
        if a[i][1]>Max:
            Max=a[i][1]
    global _Maximum_
    _Maximum_ = Max
    return Max

def Minimum():
    a = n
    Min=a[0][1]                                                                                          
    for i in range(1,len(a)):
        if a[i][1]<Min:
            Min=a[i][1]
    global _Minimum_
    _Minimum_ = Min
    return Min

def Total():
    a = n
    tot=a[0][1]
    for i in range(1,len(a)):
        tot+=a[i][1]
    global _Total_
    _Total_ = tot
    return tot

def Avarage():
    a = n
    avg=0
    tot=Total()
    avg=round(float(tot)/(len(a)), 2)
    global _Avarage_
    _Avarage_ = avg
    return avg

MaxLabel = tk.Label(root, text=f"Maximum:\t {_Maximum_}")
MinLabel = tk.Label(root, text=f"Minimum:\t {_Minimum_}")
TotalLabel = tk.Label(root, text=f"Total:\t\t {_Total_}")
AvgLAbel = tk.Label(root, text=f"Avarage:\t\t {_Avarage_}")

def EditSubjects(name, score, win):
    if name != None and name != "" and score != None:
        n.append((name, score))
        subjectsBoard.configure(state='normal')
        subjectsBoard.insert(tk.INSERT, f"\n{name}\t{score}")
        subjectsBoard.configure(state='disabled')
        MaxLabel.configure(text=f"Maximum:\t {Maximum()}")
        MinLabel.configure(text=f"Minimum:\t {Minimum()}")
        TotalLabel.configure(text=f"Total:\t\t {Total()}")
        AvgLAbel.configure(text=f"Avarage:\t\t {Avarage()}")
        win.destroy()

def AddNewSubject():
    subjectWin = tk.Toplevel()
    subjectWin.grab_set()
    subjectWin.transient(root)
    subjectNameInLabel = tk.Label(subjectWin, text="Enter subject name", padx=10, pady=10)
    subjectScoreInLabel = tk.Label(subjectWin, text="Enter marks for that subject", padx=10, pady=10)
    subjectNameInEntry = tk.Entry(subjectWin)
    subjectScoreInEntry = tk.Entry(subjectWin)
    
    def getScore():
        try:
            score = float(subjectScoreInEntry.get())
            return score
        except Exception:
            return None
    
    confirmBtn = tk.Button(subjectWin, text="add subject", padx=10, pady=10, command=lambda:EditSubjects(subjectNameInEntry.get(), getScore(), subjectWin))
    backBtn = tk.Button(subjectWin, text="cancel", padx=10, pady=10, command=subjectWin.destroy)
    
    subjectNameInLabel.pack()
    subjectNameInEntry.pack()
    subjectScoreInLabel.pack()
    subjectScoreInEntry.pack()
    confirmBtn.pack()
    backBtn.pack()
    

def RmAll():
    subjectsBoard.configure(state='normal')
    subjectsBoard.delete(1.0, tk.END)
    subjectsBoard.configure(state='disabled')
    n.clear()

subjectsNote = tk.Label(root, text="Subjects")
subjectsNote.place(anchor='c', relx=0.25, y=20)

subjectsBoard.place(x=10, y=40, relheight=0.75, relwidth=0.5)
subjectsBoard.configure(state='disabled')

addSubjectBtn = tk.Button(root, padx=10, pady=10, text="Add new subject", command=AddNewSubject)
addSubjectBtn.place(anchor='c', relx=0.125, rely=0.925, width=125, height=40)

rmAllSubjectsBtn = tk.Button(root, padx=10, pady=10, text="clear all subjects", command=RmAll)
rmAllSubjectsBtn.place(anchor='c', relx=0.375, rely=0.925, width=125, height=40)
        
saveToDiskConfirmation = tk.Label(root, fg='green')
        
def SaveToDisk():
    try:
        dir = pathlib.Path("Results")
        dir.mkdir(parents=True, exist_ok=True)
        file = open(f"{dir}/{p}.txt", 'w')
        file.write(f"Subjects - Marks:{subjectsBoard.get(1.0, tk.END)}\nMaximum: {_Maximum_}\nMinimum: {_Minimum_}\nTotal: {_Total_}\nAvarage: {_Avarage_}\n")
        file.close()
        saveToDiskConfirmation.configure(text="Saved!")
    except Exception:
        saveToDiskConfirmation.configure(fg='red', text="Saving failed!")

MaxLabel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.1)
MinLabel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.2)
TotalLabel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.3)
AvgLAbel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.4)

saveToDiskBtn = tk.Button(root, text="Save data to disk", command=SaveToDisk)
EXITbtn = tk.Button(root, text="Exit", command=lambda:sys.exit(0))

saveToDiskConfirmation.place(anchor='c', height=40, width=200, relx=0.75, rely=0.75)

saveToDiskBtn.place(anchor='c', height=40, width=200, relx=0.75, rely=0.65)
EXITbtn.place(anchor='c', height=40, width=100, relx=0.75, rely=0.85)

tk.mainloop()
