from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-350, 0)
R_PADDLE_UP_BIND = "Up" 
R_PADDLE_DOWN_BIND = "Down"
L_PADDLE_UP_BIND = "w" 
L_PADDLE_DOWN_BIND = "s"
PADDLE_COLLISION_DISTANCE = 50


def move_objects(ball, right_paddle, left_paddle):

    """Moves the ball and paddles based on their current speeds."""

    right_paddle.move()
    left_paddle.move()
    ball.move()


def handle_collisions (ball, right_paddle, left_paddle, screen):
    
    """
    Handle collisions of the ball with both paddles and top and bottom of the screen.

    - Bounce ball off the top and bottom wall.
    - Detect paddle collisions and bounce the ball off the paddle.
    - Increase speed of each bounce from paddle
    - Handle multiple bounce off paddle bug with bounce flag
    """
    
    if ball.check_wall_collision():
        ball.wall_bounce()

    if (ball.xcor() > 320 and ball.distance(right_paddle) < PADDLE_COLLISION_DISTANCE 
        and not ball.bounce_flag):
        ball.paddle_bounce()
        right_paddle.flash(screen)
        ball.increase_speed()
        ball.bounce_flag = True
        
    if (ball.xcor() < -320 and ball.distance(left_paddle) < PADDLE_COLLISION_DISTANCE 
        and not ball.bounce_flag):
        ball.paddle_bounce()
        left_paddle.flash(screen)
        ball.increase_speed()  
        ball.bounce_flag = True
        
    # Reset bounce flag once the ball is far away from paddle
    if -320 < ball.xcor() < 320:
        ball.bounce_flag = False


def process_point(ball, left_paddle, right_paddle, scoreboard): 
     
    """
    Handle situations when paddle misses the ball and the point ends.

    - Detect if paddle missed the ball.
    - Update the score based on the miss.
    - Reset positions for both paddles and ball.
    """

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()
        right_paddle.reset_position()
        left_paddle.reset_position()
        
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()
        right_paddle.reset_position()
        left_paddle.reset_position()
         
        
def main():

    """
    Initialize and run the Pong game.
    
    - Create the screen and game objects.
    - Handle user input for movement of paddles.
    - Run game loop to move ojects, handle collisions and process points.
    """

    # creating screen
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_COLOR)
    screen.title("Pong")
    screen.tracer(0)


    # initializing right, left paddle and ball
    right_paddle = Paddle(R_PADDLE_POSITION)
    left_paddle = Paddle(L_PADDLE_POSITION)
    ball = Ball()
    scoreboard = Scoreboard()


    # making the paddles ready for user interaction
    screen.listen()
    screen.onkeypress(right_paddle.start_up, R_PADDLE_UP_BIND)
    screen.onkeypress(right_paddle.start_down, R_PADDLE_DOWN_BIND)
    screen.onkeypress(left_paddle.start_up, L_PADDLE_UP_BIND)
    screen.onkeypress(left_paddle.start_down, L_PADDLE_DOWN_BIND)

    screen.onkeyrelease(right_paddle.stop_up, R_PADDLE_UP_BIND)
    screen.onkeyrelease(right_paddle.stop_down, R_PADDLE_DOWN_BIND)
    screen.onkeyrelease(left_paddle.stop_up, L_PADDLE_UP_BIND)
    screen.onkeyrelease(left_paddle.stop_down, L_PADDLE_DOWN_BIND)

    game_on = True

    while game_on:

        # update each frame
        time.sleep(0.03)
        screen.update()

        move_objects(ball, right_paddle, left_paddle)
        
        handle_collisions(ball, right_paddle, left_paddle, screen)

        process_point(ball, left_paddle, right_paddle, scoreboard)
        
    screen.exitonclick()

if __name__ == "__main__":
    main()