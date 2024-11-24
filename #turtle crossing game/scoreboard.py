from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.ubdete()

    def ubdete(self):
        self.write(f"level:{self.level}", align="left", font=FONT)

    def increase(self):
        self.clear()
        self.level+=1
        self.ubdete()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="Center", font=FONT)
