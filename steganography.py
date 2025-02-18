from tkinter import*
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry("700x500")
win.config(bg="black")
#BUTTON FUNCTION
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title="Select File Type",
                                           filetypes=(("PNG files","*.png"),("JPG files","*.jpg"),("All files","*.*")))
    if open_file:
        img = Image.open(open_file)
        img = ImageTk.PhotoImage(img)
        lf1.configure(image=img)
        lf1.image=img
    else:
        messagebox.showerror("Error", "No file selected")

def hide():
    global hide_msg
    password = code.get()
    if password =="1234":
        
        msg = text1.get("1.0",END)
        hide_msg = lsb.hide(str(open_file),msg)
        messagebox.showinfo("Success","Your message is successfully hidden in a image,please save your image")
    elif password =="":
        messagebox.showerror("Error","Please enter Secret Key")
    else:
        messagebox.showerror("Error","Wrong Secret Key")
        code.set("")
        
hide_msg = None

def save_img():
    global hide_msg
    if hide_msg:
        hide_msg.save("Secret file.png")
        messagebox.showinfo("Saved", "Image has been successfully saved")
    else:
        messagebox.showerror("Error", "No hidden message to save")

def show():
    password = code.get()
    if password == "1234":
        show_msg = lsb.reveal(open_file)
        if show_msg:
            text1.delete("1.0", END)
            text1.insert(END, show_msg)
        else:
            messagebox.showinfo("Info", "No hidden message found in the image.")
    elif password == "":
        messagebox.showerror("Error", "Please enter Secret Key")
    else:
        messagebox.showerror("Error", "Wrong Secret Key")
        code.set("")
#LOGO
logo = PhotoImage(file="logoo.png")
Label(win, image=logo, bd=0).place(x=50,y=0)

#HEADING
Label(win, text="CYBER SECURITY PROJECT", font="impact 50 bold", bg="black", fg="white").place(x=360,y=12)

#FRAME 1
f1 = Frame(win,width=350,height=220,bd=5, bg="light blue")
f1.place(x=60,y=200)
lf1 = Label(f1, bg="white")
lf1.place(x=0,y=0)

#FRAME 2
f2 = Frame(win,width=400,height=220,bd=5, bg="dark blue")
f2.place(x=450,y=200)
text1 = Text(f2,font="ariel 15 bold",wrap=WORD)
text1.place(x=0,y=0,width=450,height=220)

#LABEL FOR SECRET KEY
Label(win, text="Enter Secret Key", font="ariel 15 bold", bg="black", fg="yellow").place(x=270,y=430)

#Entry Widget for Secret Key
code=StringVar()
e = Entry(win,bd=2,font="impact 20 bold",show="*", textvariable=code)
e.place(x=240,y=470)

#BUTTONS
open_button = Button(win,text="Open Image",font="ariel 15 bold",bg="green",fg="white", cursor="hand2",command=open_img)
open_button.place(x=60,y=550)

save_button = Button(win,text="Save Image",font="ariel 15 bold",bg="dark blue",fg="white", cursor="hand2",command=save_img)
save_button.place(x=250,y=550)

hide_button = Button(win,text="Hide Data",font="ariel 15 bold",bg="red",fg="white", cursor="hand2",command=hide)
hide_button.place(x=550,y=550)

show_button = Button(win,text="Show Data",font="ariel 15 bold",bg="orange",fg="white", cursor="hand2",command=show)
show_button.place(x=700,y=550)


mainloop()