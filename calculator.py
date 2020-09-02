import tkinter as tk

root=tk.Tk()

expression = ""



def press(num):

	global expression
	expression = expression+str(num)

	equation.set(expression)

if __name__=="__main__":

	gui = tkinter()

	gui.configure(background="grey")

	gui.title("My Calculator")

	E1= Entry(gui, bd=5)
	E1.pack(side = RIGHT)
	name_entry=tk.StringVar()
	number=name_entry.get()
	print(number)

	gui.mainloop()

	#gui.geometry("270*150")




def calc(c,x,y):
	if c=="+":
		ans = x+y
		return ans
	elif c=="-":
		ans = x-y
		return ans
	elif c=="*":
		ans = x*y
		return ans
	elif c=="/":
		ans = x/y
		return ans



print("CALCULATOR")
x = int(input("Enter number 1:   "))

y = int(input("Enter number 2:   "))
c = input("Enter +,-,/,*:   ")
ans = calc(c,x,y)
print(ans)

