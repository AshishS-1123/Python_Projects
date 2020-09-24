import copy
import random

# create a class to represent the hat from which balls are drawn
class Hat:
    
    # constructor with variable keyword arguments
    def __init__(self, **kwargs):
        
        # create an empty list to hold the color of all ball present in it
        self.contents = []
        
        # for every key and data in the keyword argument,
        # get the color of ball, and how many such balls are present
        for color, number in kwargs.items():
            # for every color, add the ball as many times as it is present
            for _ in range(number):
                self.contents.append(color)
	
	# method to randomly draw a ball from the hat
    def draw(self, balls_to_draw):
        # get the number of balls present in the hat
        num_balls_present = len( self.contents ) -1
        
        # if the ball present are less than the balls needed to be drawn
        if num_balls_present <= balls_to_draw:
            # return all the balls present in the hat as they will always be drawn
            return self.contents
		
        # create an empty list to hold the balls drawn from the hat
        balls_drawn = []
        # repeat the following to draw the ball the required amount of times
        for _ in range( balls_to_draw ):
            # randomly choose a ball from the hat
            ball = random.choice(self.contents)
            # remove that ball from the hat so that it dosen't get included in further drawings
            self.contents.remove(ball)
            # add this ball to the ball_drawn list
            balls_drawn.append(ball)
            # decrement the number of balls present by 1
            num_balls_present -= 1
            
        # return the list of balls drawn
        return balls_drawn

# function to simulate the experiment of randomly drawing balls a number of times,
# to calculate the probability 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    # variable to store how may how many of the experiments were successful
    experiment_successful = 0
    
    # repeat the following for all experimants
    for _ in range( num_experiments ):
        
        # create a copy of the hats
        hat_copy = copy.deepcopy(hat)
        
        # randomly draw a number of ball from the hat
        drawn_balls = hat_copy.draw( num_balls_drawn )
        # convert the balls drawn to a dict as { color_of_ball : no_of_balls_of_this_color }
        drawn_balls = {ball : drawn_balls.count(ball) for ball in set(drawn_balls) }
        
        # variable to hold whether all the balls drawn were present in the balls drawn
        present = True
        
        # repeat the following for every expected ball
        for ball in expected_balls:
            # if one of the expected balls was not present in balls drawn
            if ball not in drawn_balls or drawn_balls[ ball ] < expected_balls[ ball ]:
                # mark expected balls as not present
                present = False
                # exit this loop
                break
                
        # if all the expected balls were present,
        if present:
            # mark this experiment as successful and increment no of successful expt by 1
            experiment_successful += 1

    # calculate the ratio of successful expt to the total expts
    probability = experiment_successful / num_experiments

    # return the calculated probability
    return probability
