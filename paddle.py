from turtle import Turtle

PADDLE_SPEED = 10
PIXEL_LIMIT = 250
PADDLE_COLOR = "white"
PADDLE_HIT_COLOR = "burlywood1"

class Paddle(Turtle):

    """Represent paddle which is movable by user interaction."""

    def __init__(self, position):

        """Initialize paddle at default position and set movement flags."""

        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(5, 1)
        self.penup()
        self.start_position = position
        self.goto(position)

        # Flags for key holding
        self.moving_up = False
        self.moving_down = False
    
    def go_up(self):

        """Move the paddle up without going beyond screen limit."""

        new_y_pos = self.ycor() + PADDLE_SPEED

        # condition so the paddle cannot go out of bonds
        if new_y_pos > PIXEL_LIMIT:
            new_y_pos = PIXEL_LIMIT 
            
        self.goto(self.xcor(), new_y_pos)
    
    def go_down(self):

        """Move the paddle down without going beyond screen limit."""

        new_y_pos = self.ycor() - PADDLE_SPEED

        # condition so the paddle cannot go out of bonds
        if new_y_pos < -PIXEL_LIMIT:
            new_y_pos = -PIXEL_LIMIT

        self.goto(self.xcor(), new_y_pos)

    def start_up(self):

        """Set flag to move paddle upwards in continuous motion."""

        self.moving_up = True
    
    def start_down(self):

        """Set flag to move paddle downwards in continuous motion."""

        self.moving_down = True
    
    def stop_up(self):

        """Set flag to stop upwards movement."""

        self.moving_up = False
    
    def stop_down(self):
        
        """Set flag to stop downwards movement."""

        self.moving_down = False
    
    def move(self):

        """Move the paddle based on current movement flags."""

        if self.moving_up:
            self.go_up()

        if self.moving_down:
            self.go_down()

    def flash(self, screen):

        """Change color of paddle temporarily to indicate that it was hit."""

        self.color(PADDLE_HIT_COLOR)
        # reset back after 100 ms
        screen.ontimer(lambda: self.color(PADDLE_COLOR), 100)
    
    def reset_position(self):

        """Reset position of paddle back to starting position."""

        self.goto(self.start_position)