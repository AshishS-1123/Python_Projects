'''
 Function : argument_parser
 Description : parses the string expression and return the operator and operands
 Parameters : expression - string representing the sum to be formatted
 Return Value : operand[0] - first operand in expression
                           operand[1] - second operand in expression
                           operator - operator to be applied to operands
'''
def argument_parser( expression ):
    # create a list with 2 items to hold the operands
    operands = [ "", "" ]
    # create a variable to hold the operator
    operator = '+'
    # create a variable to hold which operand we are currently working on
    operand_number = 0
	
    # loop through every character in the expression
    for character in expression :
        # check if the character can be converted to a number
        try :
            character = int(character)
        # if not, then it must be either a space or symbol
        except:
            # if the character is a space, continue
            if character == ' ':
                continue
		    # if the characters is a symbol,
            elif character in ['+', '-', '*', '/', '\n'] :
                # save the symbol as operator
                operator = character
                # from here on, work on the second operand
                operand_number = 1
                continue
            # if character is neighter symbol nor integer, mark operator as x for future use
            else :
                operator = "x"
                continue
        # append this character to the operand
        operands[ operand_number ] += str(character)
    
    # return the operands and the operator
    return operands[0], operands[1], operator

'''
Function : arithmatic_arranger
Description : converts the expression to the given format
Paramters : problems - list of strings containing the expression
                      evaluate - bool value indicating whether to display the answer
Return Value : string representing the expressions in the converted format
'''
def arithmetic_arranger( problems, evaluate = False ) :
    # list of strings representing four lines- operand1, operator+operand2, horizontal line, answer
    answer = [ "", "", "", "" ]
	
	# if number of problems to be processed is more than 5, return a message
    if len( problems ) > 5 :
        return "Error: Too many problems."
	
	# repeat the following for every exression in given problems
    for equation in problems :
        # parse the equation and get the operands ans operator
        operand1, operand2, operator = argument_parser( equation )
        # string representing the trailing space after every problem
        trailing_space = "    "

        # while parsing, if we encounter an unknown character, it is indicated by 'x'
        if operator == "x" :
            # inform the user that an unknown character has been encountered
            return "Error: Numbers must only contain digits."
            
        # if operator is multiplication or division
        elif operator == "*" or operator == "/" :
            # inform the user that the wrong operator has been specified
            return "Error: Operator must be '+' or '-'."
            
        # if either operand is larger than 9999,
        elif int(operand1) - 9999 > 0 or int(operand2) - 9999 > 0 : 
            # inform  the user that large operands are not allowed
            return "Error: Numbers cannot be more than four digits."
        # otherwise
        else :
            # get the number of digits in both the operands
            len1 = len( operand1 )
            len2 = len( operand2 )
			
			# write the operands, operator and the horizontal line as it is supposed to appear
			
            space_in_first_line = 2 + max(len1, len2) - len1
            answer[0] +=  " " * space_in_first_line + operand1 + trailing_space 
			
            space_in_second_line = 1 + max(len1, len2) - len2
            answer[1] += operator + " " * space_in_second_line + operand2 + trailing_space 
			
            answer[2] += "-" * (max(len1, len2) + 2) + trailing_space 
			
			# if user wants to evaluate the expression
            if evaluate is True :
                
                # if the operator is addition
                if operator == "+" :
                    # add the operands and store the result
                    result = int(operand1) + int(operand2)
                    
                # if the operator is subtraction
                else :
                    # subtract the operands and store the result
                    result = int(operand1) - int(operand2)
               
                # convert the result to string 
                result = str(result)
                
                # write the result as per the given format
                number_of_spaces = space_in_first_line + len1 - len(result)
                answer[3] += " " * number_of_spaces + result + trailing_space 
                
            # if the user dosen't want the answer
            else :
                # add spaces in the final line
                answer[3] += " " * space_in_first_line + trailing_space 
	
	# add line breaks to the final answer
    converted_problem = answer[0][:-4] +"\n" + answer[1][:-4] +"\n" + answer[2][:-4]
    
    if evaluate is True :
        converted_problem += "\n" + answer[3][:-4]
    
    # return the converted problem
    return converted_problem

