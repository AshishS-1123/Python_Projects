# Create the rectange class the represents a rectangle in our program
class Rectangle:
	
    # define the constructor
    def __init__(self, width, height):
        # set the height of the rectangle
        self.height = height
        # set the weight of the rectangle
        self.width = width
		
    # setter function to change and set the width of rectangle
    def set_width(self, new_width):
        # set the width of the rectangle to the new value
        self.width = new_width
        
    # setter function to change and set the height of rectangle
    def set_height(self, new_height):
        # set the height of the rectangle to the new value
        self.height = new_height
        
    # getter function for calculating and returning the area of the rectangle
    def get_area(self):
        # calculate the area of rectangle as per formula
        area = self.height * self.width
        # return the area
        return area
        
    # getter function for calculating and returning the perimeter of rectangle
    def get_perimeter(self):
        # calculate the perimeter of rectangle as per the formula
        perimeter =  2 * ( self.height  + self.width )
        # return the perimeter
        return perimeter
        
    # getter function for calcuating the diagonal of rectangle
    def get_diagonal(self):
        # calculate the length of diagonal as per the formula
        diagonal = (self.height ** 2  +  self.width ** 2) ** 0.5
        # return the diagonal
        return diagonal
        
    # this function draws the rectangle on the screen in the form of '*' as strings
    def get_picture(self):
        # if either height or width of rectangle is more than 50, the rectangle cannot be drawn
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
            
        # a row in the rectangle will contain as many '*' as its width
        row = "*" * self.width
        # create an empty string that denotes the picture
        picture = ""
        
        # the number of columns in image will be the same as its height
        for i in range(self.height):
            # for each column, append the row created above along with the end line character
            picture += row + "\n"
            
        # return this string
        return picture
        
    # this function calculates how many of the given shape can be fit inside this rectangle
    def get_amount_inside(self, shape):
        # get how many shapes can be fit in the width of the rectangle
        obj_along_row = self.width / shape.width
        # round down this to a whole number
        obj_along_row = int( obj_along_row )
		
		# get how many shapes can be fit in the height of the rectangle
        obj_along_col = self.height / shape.height
        # round down this to a whole number
        obj_along_col = int( obj_along_col )
		
		# the total number of shapes that can be fit is-
        amount = obj_along_row * obj_along_col
        
        # return this amount
        return amount
        
    # define the string representation of the rectangle
    def __str__(self):
        # create the string representation of the rectangle
        obj_as_string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        # return this string
        return obj_as_string

# Create the square class that inherits from the rectangle class
class Square(Rectangle):
    
    # define the constructor
    def __init__(self, side):
        # the height of square is the equal to its side
        self.height = side
        # the width of square is equal to its side
        self.width = side
        
    # setter function to set the side of square
    def set_side(self, new_side):
        # set the height equal to side
        self.height = new_side
        # set the width equal to side
        self.width = new_side
    
    # redefine the setter function for width
    def set_width(self, new_width):
        # set the height equal to the new width
        self.height = new_width
        # set the width equal to the new width
        self.width = new_width
    
    # redefine the setter function for height
    def set_height(self, new_height):
        # set the height equal to the new height
        self.height = new_height
        # set the width equal to the new height
        self.width = new_height
        
    # redefine the string representation for square
    def __str__(self):
        # create the string representation for square
        obj_as_string = "Square(side=" + str(self.width) +")"
        # return the string
        return obj_as_string
