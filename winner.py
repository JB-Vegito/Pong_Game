from turtle import Turtle
# from scoreboard import Scoreboard

class Winner(Turtle):

    def __init__(self, scoreboard):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.celebrate(scoreboard)

    def celebrate(self, scoreboard):

        self.goto(0,0)
        self.write("WINNER", align="center", font=("Courier", 80, "normal"))
        self.penup()
        self.goto(0, -100)

        if scoreboard.l_score == 5:
            self.color("red")
            self.write("RED", align="center", font=("Courier", 60, "normal"))

        elif scoreboard.r_score == 5:
            self.color("blue")            
            self.write("BLUE", align="center", font=("Courier", 60, "normal"))
                
        
        

        