from tkinter import *

class Button:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.command = 0
        self.x = 0
        self.y = 0
        self.button = 0
    
    def create_button(self, x, y, width, height, command):
        self.width = width
        self.height = height
        self.command = command
        self.x = x
        self.y = y
        self.button = screen1.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = "black")

    def click_button(self, event):
        if ((self.x < event.x < (self.x + self.width)) and (self.y < event.y < (self.y + self.height))):
            exec(self.command)

class Screen:
    def __init__(self):
        pass

    def Main_Screen(self):
        self.screen = Tk()
        self.screen.title("Guck-Bap RPG")
        self.screen.resizable(True, True)
        self.canvas = Canvas(self.screen, width = 1280, height = 720, bg = 'white')
        self.game_start = Button()
        self.game_start.create_button(490, 310, 300, 100, 'screen1.Game_Start()')
        self.screen.bind("<Button-1>", self.game_start.click_button)
        self.canvas.pack()            

    def Game_Start(self):
        self.canvas.configure(bg = '#60ff60')
        self.screen.update()
        print("Game Start")

screen1 = Screen()
screen1.Main_Screen()
screen1.screen.mainloop()
