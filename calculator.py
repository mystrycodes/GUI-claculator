from cgitb import text
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Calculator")
root.geometry("300x450")

# Text Area
text_area=tk.Entry(root,width=40,borderwidth=4)
text_area.grid(row=0,column=0,columnspan=3,padx=20,pady=2)

def number_input(num):
    prev=text_area.get()
    text_area.delete(0,tk.END)
    text_area.insert(0,prev+str(num))

def equals():
    contents=text_area.get()
    text_area.delete(0,tk.END)
    try:
        answer=eval(contents)
    except Exception:
        answer="Invalid Input"
    finally:
        text_area.insert(0,answer)

# Buttons 0-9, +-*/%= clear
btn9=tk.Button(root,text="9",padx=40,pady=20,command=lambda : number_input(9))
btn9.grid(row=1,column=0)
btn8=tk.Button(root,text="8",padx=40,pady=20,command=lambda : number_input(8))
btn8.grid(row=1,column=1)
btn7=tk.Button(root,text="7",padx=40,pady=20,command=lambda : number_input(7))
btn7.grid(row=1,column=2)
btn6=tk.Button(root,text="6",padx=40,pady=20,command=lambda : number_input(6))
btn6.grid(row=2,column=0)
btn5=tk.Button(root,text="5",padx=40,pady=20,command=lambda : number_input(5))
btn5.grid(row=2,column=1)
btn4=tk.Button(root,text="4",padx=40,pady=20,command=lambda : number_input(4))
btn4.grid(row=2,column=2)
btn3=tk.Button(root,text="3",padx=40,pady=20,command=lambda : number_input(3))
btn3.grid(row=3,column=0)
btn2=tk.Button(root,text="2",padx=40,pady=20,command=lambda : number_input(2))
btn2.grid(row=3,column=1)
btn1=tk.Button(root,text="1",padx=40,pady=20,command=lambda : number_input(1))
btn1.grid(row=3,column=2)
btn0=tk.Button(root,text="0",padx=40,pady=20,command=lambda : number_input(0))
btn0.grid(row=4,column=0)
btnadd=tk.Button(root,text="+",padx=40,pady=20,command=lambda : number_input('+'))
btnadd.grid(row=4,column=1)
btnsub=tk.Button(root,text="-",padx=40,pady=20,command=lambda : number_input('-'))
btnsub.grid(row=4,column=2)
btnmul=tk.Button(root,text="*",padx=40,pady=20,command=lambda : number_input('*'))
btnmul.grid(row=5,column=0)
btndiv=tk.Button(root,text="/",padx=40,pady=20,command=lambda : number_input('/'))
btndiv.grid(row=5,column=1)
btnmod=tk.Button(root,text="%",padx=40,pady=20,command=lambda : number_input('%'))
btnmod.grid(row=5,column=2)
btnclr=tk.Button(root,text="clear",padx=80,pady=20,command=lambda :text_area.delete(0,tk.END))
btnclr.grid(row=6,column=1,columnspan=2)
btneql=tk.Button(root,text="=",padx=40,pady=20,command=equals)
btneql.grid(row=6,column=0)

root.mainloop()