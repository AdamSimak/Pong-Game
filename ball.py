from turtle import Turtle
import time

MAX_SPEED = 15
INITIAL_SPEED = 6
SPEED_INCREMENT = 1.05
BALL_COLOR = "white"

class Ball(Turtle):

    """Represents ball and handles its movement, collisions and speed."""

    def __init__(self,):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()

        # movement attributes
        self.x_initial_speed = INITIAL_SPEED
        self.y_initial_speed = INITIAL_SPEED
        
        self.x_move_speed = self.x_initial_speed
        self.y_move_speed = self.y_initial_speed

        # flag that prevents multiple bounces with paddle
        self.bounce_flag = False

    def move(self):

        """Move the ball according to its x and y speeds."""

        new_xcor = self.xcor() + self.x_move_speed
        new_ycor = self.ycor() + self.y_move_speed
        self.goto(new_xcor, new_ycor)
    
    def check_wall_collision(self):

        """Return True if ball hits top or bottom wall."""

        if self.ycor() > 280 or self.ycor() < - 280:
            return True
    
    def wall_bounce(self):
        
        """Bounce the ball of the wall by inverting its y-direction speed."""

        self.y_move_speed *= -1 
    
    def paddle_bounce(self):

        """Bounce the ball of the paddle by inverting its x-direction speed."""

        self.x_move_speed *= -1
    
    def increase_speed(self):

        """Increase both x and y speeds, until it hits the MAX_SPEED."""

        if abs(self.x_move_speed) > MAX_SPEED:
            return
        self.x_move_speed *= SPEED_INCREMENT
        self.y_move_speed *= SPEED_INCREMENT

    def reset(self):

        """ Reset ball to center, invert initial speeds and pause briefly."""

        self.goto(0,0)
        self.x_move_speed = self.x_initial_speed * (-1 if self.x_move_speed > 0 else 1)
        self.y_move_speed = self.y_initial_speed * (-1 if self.y_move_speed > 0 else 1)
        time.sleep(1)