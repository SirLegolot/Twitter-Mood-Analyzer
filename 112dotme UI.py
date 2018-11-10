import tkinter as tk
from PIL import ImageTk, Image
from emotionAnalyzer import emotionAnalyzerRaw
from graphics import runDrawing

def init(data):
    data.inMenu = True
    data.buttonWidth = data.width//3
    data.buttonHeight = data.buttonWidth//3
    data.inputError = False
    data.loading = False
    data.twitterImage = ImageTk.PhotoImage(Image.open("Images/twitterBird112.png"))
    data.emojiImage = ImageTk.PhotoImage(Image.open("Images/emojiWeary112.png"))
    data.background = ImageTk.PhotoImage(Image.open("Images/hack112background.gif"))

def drawMenu(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "#5677fc")
    canvas.create_image(-125, -250, image = data.background, anchor = "nw")
    buttonWidth = data.buttonWidth
    buttonHeight = data.buttonHeight
    canvas.create_rectangle(data.width//2 - buttonWidth//2,
                            data.height*0.8 - buttonHeight//2,
                            data.width//2 + buttonWidth//2,
                            data.height*0.8 + buttonHeight//2,
                            fill = "#47A8E5")
    canvas.create_text(data.width//2, data.height//4,
            text = "   Welcome to Twitter Mood Analyzer!\nType in a username "+
            "to see how they've\n"+"  been feeling based on recent tweets!",
            font = "Arial " + str(data.height//20) + " bold", 
            fill = "white", anchor = "center")
    canvas.create_text(data.width//2, data.height*0.8,
            text = "Retrieve Data", anchor = "center",
            font = "Arial " + str(data.height//20) + " bold",
            fill = "white")
    canvas.create_text(data.width//3, data.height//2, text = "@",
                        font = "Arial " + str(data.height//30) + " bold",
                        fill = "white")
    canvas.create_image(data.width//5, data.height*0.8,
                        image = data.twitterImage)
    canvas.create_image(4*data.width//5, data.height*0.8,
                        image = data.emojiImage)
                            
def mousePressed(event, data, textbox):
    if data.inMenu == True:
        buttonTop = data.height*0.8 - data.buttonHeight//2
        buttonBottom = data.height*0.8 + data.buttonHeight//2
        buttonLeft = data.width//2 - data.buttonWidth//2
        buttonRight =  data.width//2 + data.buttonWidth//2
        if buttonTop < event.y < buttonBottom and \
            buttonLeft < event.x < buttonRight:
            data.loading = True
    else:
        textbox.delete('1.0', 'end')
        data.inputError = False
        init(data)
                            
def keyPressed(event, data, textbox):
    if data.inMenu and event.keysym == "Return":
        data.loading = True 

def loadingScreen(canvas, data, textbox):
    canvas.create_image(-125, -250, image = data.background, anchor = "nw")
    buttonWidth = data.buttonWidth
    canvas.create_text(data.width//2, data.height//2,
            text = "Retrieving Data, Please Wait",
            font = "Arial " + str(data.height//20) + " bold", 
            fill = "white", anchor = "center")
    canvas.update()
    try:
        # fetching twitter data
        # assert(data.text == "test" or data.text == "test2")
        # if data.text == "test":
        data.emotionsRaw = emotionAnalyzerRaw(data.text, 20)
        data.inMenu = False
    except:
        # fails if user can't be found
        textbox.delete('1.0', '1.end')
        data.inputError = True
    data.loading = False

def drawResultsScreen(canvas, data):
    runDrawing(canvas, data.text, data.emotionsRaw)
    
def redrawAll(canvas, data, textbox):
    if data.loading == True:
        loadingScreen(canvas, data, textbox)
    elif data.inMenu == True:
        drawMenu(canvas, data)
        canvas.create_window((data.width//2, data.height//2 ), 
                window=textbox)
    else:
        drawResultsScreen(canvas, data)
    if data.inputError and data.inMenu:
        canvas.create_text(data.width//2, data.height*0.6,
                            text = " Username does not exist!\nEnter an" +
                            " existing username",
                            font = "Arial " + str(data.height//30),
                            fill = "red", anchor = "center")
 
###

def updateDrawing(canvas, data, textbox):
    canvas.delete("all")
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    redrawAll(canvas, data, textbox)
    canvas.update()
    textbox.update()
    
def mousePressedWrapper(event, canvas, data, textbox):
    mousePressed(event, data, textbox)
    updateDrawing(canvas, data, textbox)
    
def keyPressedWrapper(event, canvas, data, textbox):
    keyPressed(event, data, textbox)
    updateDrawing(canvas, data, textbox)

def timerFiredWrapper(canvas, data, textbox):
    data.text = textbox.get("1.0", '1.end')
    updateDrawing(canvas, data, textbox)
    canvas.after(data.timerDelay, timerFiredWrapper, canvas, data,
        textbox)
  
def run(width=1360, height=700):
    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100
    data.text = ""

    # window
    root = tk.Tk()
    root.title("Twitter Mood Analyzer")
    root.resizable(width=False, height=False)
    data.root = root
    init(data)
    
    # canvas
    canvas = tk.Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()

    # textbox
    textbox = tk.Text(canvas, width=50, height=1, font=("Helvetica", 10),
                border = 4)
    canvas.create_window((data.width//2, data.height//2 ), 
            window=textbox)
    
    # Wrapper function event setup
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data, textbox))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data, textbox))
    timerFiredWrapper(canvas, data, textbox)
    root.mainloop()

run()