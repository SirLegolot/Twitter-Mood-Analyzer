import math
from tkinter import *
from PIL import ImageTk, Image




def runDrawing(width=1360, height=700):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    img1 = ImageTk.PhotoImage(Image.open("Images/Analytical_Emoji.png"))
    canvas.create_image(width//2, height//2, image =img1)
    img2 = ImageTk.PhotoImage(Image.open("Images/Angry_Emoji.png"))
    canvas.create_image(width//2+100, height//2+100, image =img2)
    root.mainloop()
    print("bye!")
    
runDrawing()

