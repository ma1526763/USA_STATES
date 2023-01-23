from turtle import Turtle

class NameOnMap(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_state_name_on_map(self, state_name, x_cor, y_cor, color):
        self.penup()
        self.color(color)
        self.goto(float(x_cor), float(y_cor))
        self.pendown()
        self.write(state_name)