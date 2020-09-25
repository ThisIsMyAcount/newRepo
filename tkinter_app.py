import tkinter as tk

class MyClass:
	def __init__(self, x):
		self.x = x
	def __add__(self, other):
		return int(self.x) + int(other.x)

def test_function(value1, value2):
	a = MyClass(value1)
	b = MyClass(value2)
	c = a + b
	
	print("Button clicked.")
	button['text'] = c

root = tk.Tk()
root.title('Simple App')

canvas = tk.Canvas(root, height=200, width=300)
canvas.pack()

frame = tk.Frame(root, bg='lightblue', bd = 5)
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

entry = tk.Entry(frame, bg = 'gold')
entry.pack()

entry1 = tk.Entry(frame, bg = '#f77')
entry1.pack()

button = tk.Button(frame, text = "Ok button", command=lambda: test_function(entry.get(), entry1.get()))
button.pack()

root.mainloop()
