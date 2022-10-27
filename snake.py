from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.body_parts = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.setx(START_POS[i][0])
            self.body_parts.append(new_snake)
            self.head = self.body_parts[0]

    def move(self):
        for seg_num in range(len(self.body_parts) - 1, 0, -1):
            new_pos = self.body_parts[seg_num - 1].pos()
            self.body_parts[seg_num].goto(new_pos)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def new_segment(self):
        new_snake = Turtle('square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.setpos(self.body_parts[-1].pos())
        self.body_parts.append(new_snake)

    def collide(self):
        collision = False
        if self.head.xcor() > 280 or self.head.xcor() < -280:
            collision = True
        elif self.head.ycor() > 280 or self.head.ycor() < -280:
            collision = True
        else:
            for segment in self.body_parts[1:]:
                if self.head.distance(segment) < 10:
                    collision = True
        return collision

    def new_snake(self):
        for i in self.body_parts:
            i.setx(1000)
        self.body_parts.clear()
        self.create_snake()
