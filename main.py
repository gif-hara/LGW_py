import tkinter as tk
from cell import Cell
from point import Point

root = tk.Tk()
root.title("LGW")
#root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, bg = "#000000")
canvas.pack(fill = tk.BOTH, expand = 1)

Cell(canvas, Point(0, 0))
Cell(canvas, Point(1, 1))
Cell(canvas, Point(2, 2))

root.mainloop()
