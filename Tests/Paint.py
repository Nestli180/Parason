from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.parent = "black"
        self.brish_size = 2
        self.setUI()
    
    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                            event.y - self.brush_size,
                            event.x + self.brush_size,
                            event.y + self.brush_size,
                            fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Pythonicway PyPaint")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, column=7,
        padx=5, pady=5, sticky=E+W+S+N)
        self.canv.bind("<B1-Motion>", self.draw)
    def main():
        root = Tk()
        root.geometry("850x500+300+300")
        app = Paint(root)
        root.mainloop()

    if __name__ == '__main__':
        main()

    color_lab = Label(self, text="Color: ")
    color_lab.grid(row=0, column=0, padx=6)

    red_btn = Button(self, text="Red", width=10,
                    command=lambda: self.set_color("red"))
    red_btn.grid(row=0, column=1)

    green_btn = Button(self, text="Green", width=10,
                    command=lambda: self.set_color("green"))
    green_btn.grid(row=0, column=2)