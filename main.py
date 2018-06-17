import tkinter as tk

root = tk.Tk()
root.title("LGW")
root.geometry("400x200")

canvas = tk.Canvas(root, width=300, height=200)
canvas.create_rectangle(10, 10, 30, 60, fill="yellow")
canvas.place(x=0, y=0)

root.mainloop()
