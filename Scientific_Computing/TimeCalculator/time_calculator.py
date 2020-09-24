# function to add certain duration to the time
def add_time(start, duration, start_day = None):
    
    # dictionary with day as key and day number as data
    day_to_number = { "monday" : 0, "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6 }
    # dictionary with day number as key and day as data
    number_to_day = { 0 : "monday", 1 : "tuesday", 2 : "wednesday", 3 : "thursday", 4 : "friday", 5 : "saturday", 6 : "sunday" }
	
	# get the current hour and current minute from the start time
    start_hour, start_minute = start.split(":")
    # get the minute and AM/PM from the current minute
    start_minute, interval = start_minute.split(" ")
    
    # get the hour and minute to be added to the start time from the duration term
    duration_hour, duration_minute = duration.split(":")
    
    # add the current hour and the duration hour to get the final hour
    final_hour = int(start_hour) + int(duration_hour)
    # add the final minute and the duration minute to get the final minutes
    final_minute = int(start_minute) + int(duration_minute)

    # if number of minutes is greater than 60, convert it to hours
    while final_minute > 60:
        # remove 60 from the final minutes
        final_minute -= 60
        # increment final hour by 1
        final_hour += 1
    
    # based on the value of final hour, calculate the number of days that have passed
    # create a variable to hold the number of days that have passed
    number_of_days = 0
    # create a variable to hold whether AM or PM have been toggled
    interval_toggle = False
    
    # repeat the following until the final hour is in the standard notation
    while final_hour > 12:
        # subtract 12 from the final hour
        final_hour -= 12
        # toggle the interval
        interval_toggle ^= 1
        # increment the number of days by 1
        number_of_days += 1
        
    # if final hour is 12
    if final_hour == 12:
        # toggle the interval
        interval_toggle ^= 1
        # increment the number of days by 1
        number_of_days += 1
		
    # halve the number of days, because we were incrementing them after every 12 hours
    number_of_days /= 2
	
	# if current interval is PM and it has been toggled
    if interval_toggle == True and interval == "PM":
        # make the interval AM
        interval = "AM"
        
        # if the number of days variable has a decimal part
        if number_of_days > int(number_of_days):
            # round up the number_of_days
            number_of_days = int( number_of_days + 1)

    # if the interval is AM and it was toggled 
    elif interval_toggle == True and interval == "AM":
        # make the interval PM
        interval = "PM"
        # round up the number of days
        number_of_days = int(number_of_days)
	
    # convert the final_hour, final_minute and the interval to the output format
    answer = str(final_hour) + ":"
    if final_minute < 10:
        answer += "0"
	
    answer += str(final_minute) + " " + interval
    
    if start_day != None:
        start_day = start_day.lower()
        start_day = int( day_to_number[ start_day ] + number_of_days )
        start_day %= 7
        answer += ", " + number_to_day[ start_day ].capitalize()
    
    if number_of_days == 1:
        answer += " (next day)"
    elif number_of_days > 1:
        answer += " (" + str(number_of_days) + " days later)"
    
    # return the final answer
    return answer
