class Colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented

red = Colors('Красный', 255, 0, 0)
green = Colors ('Зелёный', 0, 255, 0)
otherRed = Colors('Другой красный', 255, 0, 0)

print(otherRed)
print(red)
print(green)

print(red==green)
print(red==otherRed)

from tkinter import *
root = Tk()
root.title("Граф примитивы")
root.minsize (width=500, height=400)
canv = Canvas (root,width=500, height=400,  bg='lightgray', cursor='pencil')
x = 50
y = 300
canv.create_rectangle (x, y, x+80, y+50, fill="white", outline="blue")
canv.pack()
root.mainloop()