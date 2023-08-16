from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        xposition = 20
        for i in range(3):
            xposition -= 20
            snake_piece = Turtle("square")
            snake_piece.penup()
            snake_piece.color("red")
            snake_piece.setposition(x=xposition, y=0)
            self.snake.append(snake_piece)

    def extend(self):
        new_xpos = self.snake[len(self.snake) - 1].xcor()
        new_ypos = self.snake[len(self.snake) - 1].ycor()
        snake_piece = Turtle("square")
        snake_piece.penup()
        snake_piece.color("red")
        snake_piece.setposition(new_xpos - 20, new_ypos - 20)
        self.snake.append(snake_piece)
    
    def move(self):
        for piece_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece_num - 1].xcor()
            new_y = self.snake[piece_num - 1].ycor()
            self.snake[piece_num].goto(new_x, new_y)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # def wall(self):
    #     if self.head.xcor() >= 290 or self.head.xcor() <= -290:
    #         self.head.setx(-self.head.xcor())
    #     elif self.head.ycor() >= 290 or self.head.ycor() <= -290:
    #         self.head.sety(-self.head.ycor())
    
    def wall(self):
        if self.head.xcor() >= 290 or self.head.xcor() <= -290:
            return True
        elif self.head.ycor() >= 290 or self.head.ycor() <= -290:
            return True

    def collide_tail(self):
        for i in range(1,len(self.snake)-1):
            if self.head.distance(self.snake[i]) <= 13:
                return True
            
    def reset(self):
        for piece in self.snake:
            piece.goto(2000,2000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]