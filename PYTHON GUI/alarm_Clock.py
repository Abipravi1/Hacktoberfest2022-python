"""Alarm Clock
Description
You're trying to automate your alarm clock by writing a function for it. You're given a day of the week encoded as 1=Mon, 2=Tue, ... 6=Sat, 7=Sun, and whether you are on vacation as a boolean value (a boolean object is either True or False. Google "booleans python" to get a better understanding). 
Based on the day and whether you're on vacation,
write a function that returns a time in form of a string indicating when the alarm clock should ring. 

When not on a vacation, on weekdays, the alarm should ring at "7:00" and on the weekends 
(Saturday and Sunday) it should ring at "10:00". 

While on a vacation, it should ring at "10:00" on weekdays. 
On vacation, it should not ring on weekends, that is, it should return "off".

----------------------------------------------------------------------
Input:
The input will be a list of two elements. The first element will be an integer from 1 to 7,
and the second element will be a boolean value."""

import ast
input_str = input()  #Give Input like this way --> ["7","True"] 

#ast.literal_eval() will evaluate the string and make a data structure for the same
#here the input is a list since input is in '[...]', so ast.literal_eval() will
#make a list with the same data as passed
input_list = ast.literal_eval(input_str)

#the data or the two values in list is now changed to separate variables
day_of_the_week = input_list[0] #first element is an integer denoting the day of the week
is_on_vacation = input_list[1]
week_end=[6,7]

if is_on_vacation:
    if day_of_the_week in week_end:
        print("Off")
    else:
        print("10:00 AM")
else:
    if day_of_the_week in week_end:
        print("10:00 AM")
    else:
        print("7:00 AM")                