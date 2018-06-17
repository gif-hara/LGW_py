import tkinter as tk
from cell import Cell
from point import Point

c = Cell(Point(13, 65))

root = tk.Tk()
root.title("LGW")
root.geometry("400x200")

canvas = tk.Canvas(root, width=300, height=200)
canvas.create_rectangle(10, 10, 30, 60, fill="yellow")
canvas.place(x=0, y=0)

label = tk.Label(root, text = "Hello world")
label.grid()

root.mainloop()
