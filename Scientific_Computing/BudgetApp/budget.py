# this class defines objects based on different budget categories
class Category :
	
    # define the constructor
    def __init__(self, category_name) :
        # set the name of the catagory
        self.category_name = category_name
        # initialize the ledger to empty dictionary. it holds the list of all transactions in this category
        self.ledger = []
        # initialize the current balance in this category
        self.amount = 0
		
    # method that checks whether this category has enough balance left for trans
    def check_funds(self, amount) : 
    # if the amount needed is present in this category
        if self.amount >= amount : 
            # return true
            return True
        # if the amount needed is not present in this category
        else :
            # return false
            return False
    
    # function to deposit the given amount in the ledger describe its purpose
    def deposit( self, amount, description = "" ) :
        # create a dictionary, first element is the amount deposited, second is the description
        deposit_info = { "amount": amount, "description": description }
        # add this information to the ledger
        self.ledger.append( deposit_info )
        # increment the amount present in this category
        self.amount += amount
    
    # function to withdraw amount from this category and give its description
    def withdraw( self, amount, description = "" ) :
        
        # check if sufficient amount is present
        if not self.check_funds(amount) :
            # if not, return false (that the transaction could not be completed)
            return False
            
        # create a dictionary, first element is amount deposited second is the description
        withdraw_info = { "amount": -1 * amount, "description": description }
        # add this information to the ledger
        self.ledger.append( withdraw_info )
        # decrement the amount present in this category
        self.amount -= amount
        # return true (that the transaction was successful)
        return True

    # getter method to get the amount present in this category
    def get_balance(self, ) :
        # return the amount present in this category
        return self.amount

    # function to transfer amount from this category to another
    def transfer(self, amount, destination) :
        
        # check if there are sufficient funds to complete the transfer
        if self.check_funds(amount) :
            # create a description for this category
            description = "Transfer to " + destination.category_name
            # withdraw the amount along with its description from this category
            self.withdraw(amount, description)
            # create a description for the destination category
            description = "Transfer from " + self.category_name
            # deposit the amount and the description to the destination category
            destination.deposit(amount, description)
            # return true (the transaction was successful)
            return True
        
        # if enough funds were not available
        else :
            # return false (the transaction was not successful)
            return False

    # create function for string representation for the catagory
    def __str__(self) :
        number_of_stars = ( 30 - len(self.category_name) ) / 2
        number_of_stars = int( number_of_stars )
        return_value = "*" * number_of_stars + self.category_name + "*" * number_of_stars + "\n"

        for expence in self.ledger :
            description = expence["description"][:23]
            amount = "{0:.2f}".format( expence["amount"] )
            number_of_spaces = 30 - len(description) - len(amount)
            return_value += description + " " * number_of_spaces + amount + "\n"

        return_value += "Total: " + str(self.amount)
        return return_value

# function to create a bargraph in terminal showing the expences for each of the categories
def create_spend_chart(category_list):
	
    max_length = max( len(category.category_name) for category in category_list )
    
    bar_chart = [
    ['1', '0', '0', '|'],
    [' ', '9', '0', '|'],
    [' ', '8', '0', '|'],
    [' ', '7', '0', '|'],
    [' ', '6', '0', '|'],
    [' ', '5', '0', '|'],
    [' ', '4', '0', '|'],
    [' ', '3', '0', '|'],
    [' ', '2', '0', '|'],
    [' ', '1', '0', '|'],
    [' ', ' ', '0', '|'],
    ]
    for row in bar_chart :
        for i in range(3 * len(category_list) + 1 ) :
            row.append(" ")

    list_ = [" ", " ", " ", " "]
    bar_chart.append(list_)
    
    for i in range( 3 * len(category_list) + 1 ) :
        bar_chart[11].append("-")
		
    for i in range(max_length) :
        list_ = [" ", " ", " ", " ", " "]
        for i in range(len(category_list)) :
            list_.append(" ")
            list_.append(" ")
            list_.append(" ")

        bar_chart.append(list_)
		
    row = 12
    col = 5
    for item in category_list :
        for char in item.category_name :
            bar_chart[row][col] = char
            row += 1
        row = 12
        col += 3
	
    # add bars to bar_chart
    row = 10
    col = 5
    bar_height = []
    total = 0
	
    for item in category_list :
        curr_with = 0
        for expence in item.ledger :
            if expence["amount"] < 0 :
                curr_with -= expence["amount"]
        bar_height.append(curr_with)

    for item in bar_height :
        total += item

    bar_height  = [ 1 + int(item*10/total) for item in bar_height ]

    for height in bar_height:
        for i in range(height):
            bar_chart[row][col] = "o"
            row -= 1
        row = 10
        col += 3

    return_value = "Percentage spent by category\n"
    # convert bar_chart list to string
    for row in bar_chart :
        for value in row :
            return_value += value
        return_value += "\n"

    return return_value[:-1]

