from turtle import Turtle


class GenerateText(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.penup()
        self.state = state
        self.goto(x, y)
        self.color("black")
        self.shape("blank")
        self.write_state()

    def write_state(self):
        self.write(f"{self.state}", align="center", font=("Arial", 12, "normal"))
