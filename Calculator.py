from tkinter import *
from tkinter import ttk

# cores

cor1 = "#d9dbda" #Silver
cor2 = "#FFAB40" #Orange
cor3 = "#ffffff" #White
cor4 = "#6aa7f7" #Blue Clear




window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg='black')

# Frames


frame_tela = Frame(window, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)
frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# Variables

all_values = ''

# Functions 

    #Input numbers in Screen
def entry_values(values):
    #Make the global values
    global all_values 

    all_values += str(values)

    #Input valors from screen
    values_text.set(all_values)

    #Calculate numbers in Screen
def calculate():
    result = eval(all_values)
    values_text.set(result)

    #Clear numbers in Screen
def clear_screen():
    global all_values
    all_values = ''
    values_text.set('')




# Label

values_text = StringVar()
create_label = Label(frame_tela, textvariable=values_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor1)
create_label.place(x=0, y=0)


# Buttons

b_1 = Button(frame_body, text="%", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('%'))
b_1.place(x=0, y=0)
b_2 = Button(frame_body, text="C", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= clear_screen)
b_2.place(x=118, y=0)
b_3 = Button(frame_body, text="/", width=5, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('/'))
b_3.place(x=177, y=0)

b_4 = Button(frame_body, text="7", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('7'))
b_4.place(x=0, y=52)
b_5 = Button(frame_body, text="8", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('8'))
b_5.place(x=59, y=52)
b_6 = Button(frame_body, text="9", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('9'))
b_6.place(x=118, y=52)
b_7 = Button(frame_body, text="*", width=5, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('*'))
b_7.place(x=177, y=52)

b_8 = Button(frame_body, text="4", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('4'))
b_8.place(x=0, y=104)
b_9 = Button(frame_body, text="5", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('5'))
b_9.place(x=59, y=104)
b_10 = Button(frame_body, text="6", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('6'))
b_10.place(x=118, y=104)
b_11 = Button(frame_body, text="+", width=5, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('+'))
b_11.place(x=177, y=104)

b_12 = Button(frame_body, text="3", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('3'))
b_12.place(x=0, y=156)
b_13 = Button(frame_body, text="2", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('2'))
b_13.place(x=59, y=156)
b_14 = Button(frame_body, text="1", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('1'))
b_14.place(x=118, y=156)
b_15 = Button(frame_body, text="-", width=5, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('-'))
b_15.place(x=177, y=156)

b_1 = Button(frame_body, text="0", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('0'))
b_1.place(x=0, y=208)
b_2 = Button(frame_body, text=".", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entry_values('.'))
b_2.place(x=59, y=208)
b_3 = Button(frame_body, text="=", width=11, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= calculate)
b_3.place(x=118, y=208)

window.mainloop()
