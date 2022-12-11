
import tkinter
from tkinter import *

app=Tk()
app.title("Manan's Calculator")
app.geometry('500x500')
app.resizable(False,False)
app.configure(bg="black")

display=Label(app,width=50,height=4,anchor="e",font=("arial",15),text="")
display.pack()

Button(app,text='AC',width=5,height=14,font=("arial",15,"bold"),bd=1,fg="black",bg="lightblue",command=lambda:ac()).place(x=15,y=125)

Button(app,text='7',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('7')).place(x=115,y=125)
Button(app,text='8',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('8')).place(x=215,y=125)
Button(app,text='9',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('9')).place(x=315,y=125)
Button(app,text='÷',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('÷')).place(x=415,y=125)

Button(app,text='4',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('4')).place(x=115,y=225)
Button(app,text='5',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('5')).place(x=215,y=225)
Button(app,text='6',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('6')).place(x=315,y=225)
Button(app,text='×',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('×')).place(x=415,y=225)

Button(app,text='1',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('1')).place(x=115,y=325)
Button(app,text='2',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('2')).place(x=215,y=325)
Button(app,text='3',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('3')).place(x=315,y=325)
Button(app,text='-',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('-')).place(x=415,y=325)

Button(app,text='0',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('0')).place(x=115,y=425)
Button(app,text='.',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('.')).place(x=215,y=425)
Button(app,text='=',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="black",bg="lightgreen",command=lambda:equate()).place(x=315,y=425)
Button(app,text='+',width=5,height=2,font=("arial",15,"bold"),bd=1,fg="lightgreen",bg="grey",command=lambda:show('+')).place(x=415,y=425)

display_str=""
equation=""

def ac():
	global display_str
	global equation
	display_str=""
	equation=""
	display.configure(text=display_str)

def show(value):
	global display_str
	global equation
	display_str+=value

	if(value=='×'):
		equation+='*'
	elif(value=='÷'):
		equation+='/'
	else:
		equation+=value
	
	display.configure(text=display_str)

def equate():
	global equation
	global display_str

	if(equation!=""):
		try:
			equation=str(eval(equation))
		except:
			equation="error"

	display_str=equation
	display.configure(text=display_str)
	
	if(equation=="error"):
		display_str=""
		equation=""

app.mainloop()