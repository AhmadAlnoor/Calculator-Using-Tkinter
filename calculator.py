from tkinter import *

root = Tk()
root.title("Simple Calculator")

input_field = Entry(root, width=25, borderwidth= 5)
input_field.grid(row=0,column=0,columnspan=4, sticky = W+E)



def button_click(number):
	current = input_field.get()
	input_field.delete(0,END)
	input_field.insert(0, str(current) + str(number))

def button_add():
	global first_number
	first_number  = int(input_field.get())
	input_field.delete(0,END)

def equals():
	second_number = int(input_field.get())
	input_field.delete(0,END)
	input_field.insert(0, first_number + second_number)


def clear():
	input_field.delete(0,END)




number_1 = Button(root, text = "1", width = 5, command=lambda: button_click(1))
number_2 = Button(root, text = "2", width = 5, command=lambda: button_click(2))
number_3 = Button(root, text = "3", width = 5, command=lambda: button_click(3))
number_4 = Button(root, text = "4", width = 5, command=lambda: button_click(4))
number_5 = Button(root, text = "5", width = 5, command=lambda: button_click(5))
number_6 = Button(root, text = "6", width = 5, command=lambda: button_click(6))
number_7 = Button(root, text = "7", width = 5, command=lambda: button_click(7))
number_8 = Button(root, text = "8", width = 5, command=lambda: button_click(8))
number_9 = Button(root, text = "9", width = 5, command=lambda: button_click(9))
number_0 = Button(root, text = "0", width = 10, command=lambda: button_click(0))
number_add = Button(root, text = "+", width = 5, command = button_add)
number_subtract = Button(root, text = "-", width = 5)
number_multiply = Button(root, text = "*", width = 5)
number_divide = Button(root, text = "/", width = 5)
equal_button = Button(root, text = "=", width = 5, command = equals)
dot_button = Button(root, text = ".", width = 5)
sign_button = Button(root, text = "+/-", width = 5)
clear_button = Button(root, text = "clear",width = 30, background = 'white', command = clear)



number_1.grid(row = 3, column = 0, padx = 4, pady = 4)
number_2.grid(row = 3, column = 1, padx = 4, pady = 4)
number_3.grid(row = 3, column = 2, padx = 4, pady = 4)
number_add.grid(row = 3, column = 3, padx = 4, pady = 4)

number_4.grid(row = 2, column = 0, padx = 4, pady = 4)
number_5.grid(row = 2, column = 1, padx = 4, pady = 4)
number_6.grid(row = 2, column = 2, padx = 4, pady = 4)
number_subtract.grid(row = 2, column = 3, padx = 4, pady = 4)

number_7.grid(row = 1, column = 0, padx = 4, pady = 4)
number_8.grid(row = 1, column = 1, padx = 4, pady = 4)
number_9.grid(row = 1, column = 2, padx = 4, pady = 4)
number_multiply.grid(row = 1, column = 3, padx = 4, pady = 4)

sign_button.grid(row = 4, column = 0, padx = 4,pady = 4)
number_0.grid(row = 4, column = 1, padx = 4,pady = 4)
dot_button.grid(row = 4, column = 2, padx = 4,pady = 4)
equal_button.grid(row = 4, column = 3, padx = 4,pady = 4)

clear_button.grid(row = 5, column = 0, columnspan = 4)




root.mainloop()