import math
from tkinter import *
from PIL import ImageTk, Image

def draw(canvas, width, height, emotions, username):
    background = ImageTk.PhotoImage(Image.open("Images/background_1360x700.jpg"))
    canvas.create_image(width/2, height/2, image = background)
    canvas.background = background
    r = (3/8) * min(width, height)
    curMax = 0
    curMax2 = 0
    maxEmotion1 = None
    maxEmotion2 = None
    for maxNum in emotions:
        if maxNum[1] > curMax:
            curMax = maxNum[1]
            maxEmotion1 = maxNum[0]
        elif maxNum[1] > curMax2:
            curMax2 = maxNum[1]
            maxEmotion2 = maxNum[0]
            
    img1 = ImageTk.PhotoImage(Image.open("Images/"+maxEmotion1+"_Emoji_150x150.png"))
    img2 = ImageTk.PhotoImage(Image.open("Images/"+maxEmotion2+"_Emoji_150x150.png"))
    canvas.create_image(width*3/4-120, height*1/3, image = img1)
    canvas.create_image(width*3/4+120, height*1/3, image = img2)
    canvas.img1 = img1
    canvas.img2 = img2
    
    if maxEmotion1 == "Anger":
        word1 = "angry"
    if maxEmotion1 == "Joy":
        word1 = "happy"
    if maxEmotion1 == "Fear":
        word1 = "scared"
    if maxEmotion1 == "Analytical":
        word1 = "insightful"
    if maxEmotion1 == "Tentative":
        word1 = "hesitant"
    if maxEmotion1 == "Sadness":
        word1 = "sad"
    if maxEmotion2 == "Anger":
        word2 = "angry"
    if maxEmotion2 == "Joy":
        word2 = "happy"
    if maxEmotion2 == "Fear":
        word2 = "scared"
    if maxEmotion2 == "Analytical":
        word2 = "insightful"
    if maxEmotion2 == "Tentative":
        word2 = "hesitant"
    if maxEmotion2 == "Sadness":
        word2 = "sad"
    canvas.create_text(width*3/4, height*2/3, text = "Based on recent tweets", font = "Courier 30")
    canvas.create_text(width*3/4, height*2/3+50, text = username+" is feeling", font = "Courier 30")
    canvas.create_text(width*3/4, height*2/3+100, text = word1+" and "+word2, font = "Courier 30")
    
    centerX = width / 3.7
    centerY = height / 2
    points = []
    polygons = []
    easyLine = []
    for i in range (6):
        angle = i*math.pi/3
        pointTxt = (centerX + math.cos (angle) * (r+45), centerY - math.sin(angle) * (r+45))
        canvas.create_text(pointTxt, text = emotions[i][0], fill = "black", font = "Courier 20 bold")
        point = (centerX + math.cos (angle) * r, centerY - math.sin(angle) * r)
        newR = (r-2) * (emotions[i][1] / curMax)
        if newR == 0:
            newR = 10
        poly = (centerX + math.cos (angle) * newR, centerY - math.sin(angle) * newR)
        
        polygons.append (poly)
        points.append (point)

    canvas.create_polygon (points, fill="light cyan", outline ="black" , width = 4)
    canvas.create_polygon (polygons, fill = "light pink", outline = "tomato", width = 3)
    
    for i in range (6) :
        angle = i*math.pi/3
        for x in range (1,5) :
            pointTick = (centerX + math.cos (angle) * (r*x / 5), centerY - math.sin(angle) * (r*x / 5))
            canvas.create_oval (pointTick[0] - 2, pointTick[1] - 2, pointTick[0] + 2, pointTick[1] + 2, fill = "black")
        point = (centerX + math.cos (angle) * r, centerY - math.sin(angle) * r)
        canvas.create_line (centerX, centerY, point[0], point[1], fill = "black", width = 1)
        canvas.create_oval (polygons[i][0] - 5, polygons[i][1] - 5, polygons[i][0] + 5, polygons[i][1] + 5, fill = "tomato")
    
    
        
        

def runDrawing(canvas, username, emotions, width=1360, height=700):
    # root = Tk()
    # root.title(username+" "+"Analysis")
    # root.resizable(width=False, height=False) # prevents resizing window
    # canvas = Canvas(root, width=width, height=height)
    # canvas.configure(bd=0, highlightthickness=0)
    # canvas.pack()
    draw(canvas, width, height, emotions, username)
    # root.mainloop()
    # print("bye!")
    

# runDrawing (emotions) 