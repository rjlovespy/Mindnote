import os, shlex
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfile, asksaveasfilename


def FileMenu():
    global F1
    def newFile(event):
        title["text"] = "Untitled - Mindnote [Version 0.1]"
        textArea.delete(1.0, END)
        F1.destroy()
    def openFile(event):
        """Return datatype is object that has name=filename, mode="r", encoding=not utf-8"""
        file = askopenfile(filetypes=[("Text File","*.txt"),("All Files","*.*")])
        if file == None:
            pass
        else:
            title["text"] = f"{os.path.basename(file.name)} - Mindnote [Version 0.1]"
            """Deletes everything from the 0th column of the 1st line to the last character's index"""
            textArea.delete(1.0, END)
            fo = open(file.name, "r")
            """Inserts file conetent at the 0th column of 1st line"""
            textArea.insert(1.0, fo.read())
            fo.close()
        F1.destroy()
    def saveFile(event):
        """Return datatype is string & it contains saved file's path that can only be accessed via mode="w" """
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", 
                                                     filetypes=[("Text File","*.txt"),("All Files","*.*")])
        if file == "":
            pass
        else:
            title["text"] = f"{os.path.basename(file)} - Mindnote [Version 0.1]"
            fo = open(file, "w")
            fo.write(textArea.get(1.0, END))
            fo.close()
        F1.destroy()
    def ExitMenuFrame():
        F1.destroy()
    
    F1 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
    F1.place(x=60, y=47, width=100, height=165)
    root.bind("<Control-n>", newFile)
    root.bind("<Control-o>", openFile)
    root.bind("<Control-s>", saveFile)
    B1 = Button(F1, text= "New", fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT)
    B1.grid(row=0, column=0, sticky=W, ipady=5)
    B1.bind("<Button-1>", newFile)
    B2 = Button(F1, text= "Open", fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT)
    B2.grid(row=1, column=0, sticky=W)
    B2.bind("<Button-1>", openFile)
    B3 = Button(F1, text= "Save", fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT)
    B3.grid(row=2, column=0, sticky=W, ipady=5)
    B3.bind("<Button-1>", saveFile)
    Button(F1, text= "Exit", command=ExitMenuFrame, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=3, column=0, sticky=W)
    

def EditMenu():
    global F2
    def cut():
        textArea.event_generate("<<Cut>>")
        F2.destroy()
    def copy():
        textArea.event_generate("<<Copy>>")
        F2.destroy()
    def paste():
        textArea.event_generate("<<Paste>>")
        F2.destroy()
    def ExitEditFrame():
        F2.destroy()
    
    F2 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
    F2.place(x=118, y=47, width=100, height=165)
    Button(F2, text= "Cut", command=cut, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=0, column=0, sticky=W, ipady=5)
    Button(F2, text= "Copy", command=copy, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=1, column=0, sticky=W)
    Button(F2, text= "Paste", command=paste, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=2, column=0, sticky=W, ipady=5)
    Button(F2, text= "Exit", command=ExitEditFrame, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=3, column=0, sticky=W)
    
    
def SettingMenu():
    global F3
    def FontFamily():
        global F
        def cancelFontFamily():
            F.destroy()
        def selectFontFamily():
            family = lstbox.get(lstbox.curselection())
            list1.append(family)
            textArea["font"] = (family, list2[-1], list3[-1])
            fontFamily["text"] = f"Font Family: {family}"
            F.destroy()
        F = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
        F.place(x=178, y=47, width=200, height=300)
        lstbox = Listbox(F, fg="#FFFFFA", bg="#141414", justify=CENTER, relief=FLAT, width=20, height=10, font="Helvetica 12 bold")
        lstbox.pack(pady=20)
        lst = ["Freestyle Script","SimSun","Palatino Linotype","Arial","Helvetica","Lucida Handwriting","French Script MT","Times New Roman","Comic Sans MS","Lucida Console"]
        for i in range(len(lst)):
            lstbox.insert(i+1, lst[i])
        Button(F, text="Cancel", command=cancelFontFamily, fg="#FFFFFA", bg="crimson", font="Helvetica 12 bold", width=7, bd=3, relief=SUNKEN).pack(side=LEFT, padx=5, pady=5)
        Button(F, text="Select", command=selectFontFamily, fg="#FFFFFA", bg="deepskyblue", font="Helvetica 12 bold", width=7, bd=3, relief=SUNKEN).pack(side=RIGHT, padx=5, pady=5)
        F3.destroy()  
    def FontSize():
        global f
        def cancelFontSize():
            f.destroy()
        def selectFontSize():
            size = lstbox.get(lstbox.curselection())
            list2.append(size)
            textArea["font"] = (list1[-1], size, list3[-1])
            fontSize["text"] = f"Font Size: {size}"
            f.destroy()
        f = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
        f.place(x=178, y=47, width=200, height=500)
        lstbox = Listbox(f, fg="#FFFFFA", bg="#141414", justify=CENTER, relief=FLAT, width=10, height=20, font="Helvetica 12 bold")
        lstbox.pack(pady=20)
        lst = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        for i in range(len(lst)):
            lstbox.insert(i+1, lst[i])
        Button(f, text="Cancel", command=cancelFontSize, fg="#FFFFFA", bg="crimson", font="Helvetica 12 bold", width=7, bd=3, relief=SUNKEN).pack(side=LEFT, padx=5, pady=5)
        Button(f, text="Select", command=selectFontSize, fg="#FFFFFA", bg="deepskyblue", font="Helvetica 12 bold", width=7, bd=3, relief=SUNKEN).pack(side=RIGHT, padx=5, pady=5)
        F3.destroy()
    def FontStyle():
        global frame
        def cancelFontStyle():
            frame.destroy()
        def selectFontStyle():
            style = lstbox.get(lstbox.curselection())
            list3.append(style)
            textArea["font"] = (list1[-1],list2[-1],style)
            fontStyle["text"] = f"Font Style: {style}"
            frame.destroy()
        frame = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
        frame.place(x=178, y=47, width=200, height=162)
        lstbox = Listbox(frame, fg="#FFFFFA", bg="#141414", justify=CENTER, relief=FLAT, width=12, height=4, font="Helvetica 12 bold")
        lstbox.pack(pady=20)
        lst = ["normal","bold","italic","bold italic"]
        for i in range(len(lst)):
            lstbox.insert(i+1, lst[i])
        Button(frame, text="Cancel", command=cancelFontStyle, fg="#FFFFFA", bg="crimson", font="Helvetica 12 bold", width=7, bd=3, relief=SUNKEN).pack(side=LEFT, padx=5, pady=5)
        Button(frame, text="Select", command=selectFontStyle, fg="#FFFFFA", bg="deepskyblue", font="Helvetica 12 bold", width=7, bd=3, relief=SUNKEN).pack(side=RIGHT, padx=5, pady=5)
        F3.destroy()
    def ExitSettingFrame():
        F3.destroy()
    
    F3 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
    F3.place(x=178, y=47, width=125, height=165)
    Button(F3, text= "Font Family", command=FontFamily, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=0, column=0, sticky=W, ipady=5)
    Button(F3, text= "Font Size", command=FontSize, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=1, column=0, sticky=W)
    Button(F3, text= "Font Style", command=FontStyle, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=2, column=0, sticky=W, ipady=5)
    Button(F3, text= "Exit", command=ExitSettingFrame, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=3, column=0, sticky=W)


def HelpMenu():
    global F4
    def Instructions():
        fo = open("E:\\GUI Development\\News\\Mindnote_instruction.txt","r")
        tmsg.showinfo(title="User Manual", message=fo.read())
        F4.destroy()
    def About():
        fo = open("E:\\GUI Development\\News\\Mindnote_about.txt","r")
        tmsg.showinfo(title="Details", message=fo.read())
        F4.destroy()
    def ExitHelpFrame():
        F4.destroy()
    
    F4 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
    F4.place(x=263, y=47, width=125, height=122)
    Button(F4, text= "Instructions", command=Instructions, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=0, column=0, sticky=W, ipady=5)
    Button(F4, text= "About", command=About, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=1, column=0, sticky=W)
    Button(F4, text= "Exit", command=ExitHelpFrame, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).grid(row=2, column=0, sticky=W, ipady=5)


def ExitWindow():
    root.destroy()
    
    
def WordCount(event): 
    # shlex.split(string) returns a list of words present in a string where string can be punctuation marks or special characters. 
    # string.split() also does the same but the string cannot be punctuation marks or special characters.
    wordCount["text"] = f"Number of words: {len(shlex.split(textArea.get(1.0, END)))}"
        
          
root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.overrideredirect(True)
list1, list2, list3 = ["Helvetica"], [14], ["normal"]


# Menubar and Titlebar
f1 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
f1.pack(fill=X)
logo = PhotoImage(file="E:\\GUI Development\\News\\Mindnote.png")
Label(f1, image=logo, bg="#141414").pack(side=LEFT, padx=15, pady=5)
Button(f1, text="File", command=FileMenu, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).pack(side=LEFT, pady=5)
Button(f1, text="Edit", command=EditMenu, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).pack(side=LEFT, padx=15, pady=5)
Button(f1, text="Setting", command=SettingMenu, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).pack(side=LEFT, pady=5)
Button(f1, text="Help", command=HelpMenu, fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold", relief=FLAT).pack(side=LEFT, padx=15, pady=5)
title = Label(f1, text="Untitled - Mindnote [Version 0.1]", fg="#FFFFFA", bg="#141414", font="Helvetica 12 bold")
title.pack(side=LEFT, padx=325, pady=5)
Button(f1, text="X", command=ExitWindow, fg="#FFFFFA", bg="crimson", font="Helvetica 12 bold", width=4, bd=3, relief=SUNKEN).pack(side=RIGHT, padx=15, pady=5)


# Text Area
f2 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
f2.pack(expand=1, fill=BOTH)
textArea = Text(f2, font="Helvetica 14", fg="#FFFFFA", bg="#141414", undo=True, maxundo=100, cursor="arrow", insertbackground="#FFFFFA", relief=FLAT)
textArea.pack(expand=1, fill=BOTH)
scrollbar = Scrollbar(textArea, jump=True)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textArea.yview)
textArea.config(yscrollcommand=scrollbar.set)


# Taskbar
f3 = Frame(root, bg="#141414", highlightbackground="#FFFFFA", highlightthickness=1)
f3.pack(side=BOTTOM, fill=X)
wordCount = Label(f3, text=f"Number of words: {len(shlex.split(textArea.get(1.0, END)))}", fg="#FFFFFA", bg="#141414",font="Helvetica 12 bold")
wordCount.pack(side=LEFT, padx=15, pady=5)
textArea.bind("<KeyPress>", WordCount)
fontFamily = Label(f3, text="Font Family: Helvetica", fg="#FFFFFA", bg="#141414",font="Helvetica 12 bold")
fontFamily.pack(side=LEFT, pady=5)
fontSize = Label(f3, text="Font Size: 14", fg="#FFFFFA", bg="#141414",font="Helvetica 12 bold")
fontSize.pack(side=LEFT, padx=15, pady=5)
fontStyle = Label(f3, text="Font Style: normal", fg="#FFFFFA", bg="#141414",font="Helvetica 12 bold")
fontStyle.pack(side=LEFT, pady=5)


FileMenu()
root.mainloop()
