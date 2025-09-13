from turtle import Turtle

SCORE_COLOR = "white"
LEFT_SCORE_POSITION = (-100, 200)
RIGHT_SCORE_POSITION = (100, 200)
SCORE_FONT = "Consolas"
SCORE_SIZE = 70

class Scoreboard(Turtle):

    """Represents scoreboard which handles score for both players."""

    def __init__(self):

        """Initialize scoreboard with left and right scores set to zero."""

        super().__init__()
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()


    def update_score(self):

        """Clear previous score and display current scores for both players."""
        
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.left_score, align="center", font=(SCORE_FONT, SCORE_SIZE, "normal"))
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.right_score, align="center", font=(SCORE_FONT, SCORE_SIZE, "normal"))

    def left_point(self):

        """Increase left player score and update it."""

        self.left_score += 1
        self.update_score()

    def right_point(self):

        """Increase right player score and update it."""

        self.right_score += 1
        self.update_score()