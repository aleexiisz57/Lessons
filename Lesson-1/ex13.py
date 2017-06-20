from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first 
print "Your second variable is:", second
print "Your third variable is:", third

# When i give fewer tahn three arguments the error tells me that
# It needs more than 3 values to unpack, so if i only give two arguments or 1
# It wont work untill a 3rd arugment is added.

#example with less arguments
from sys import argv 

script, python, note_editor = argv 

print "This script is called:", script 
print "It's written in:", python
print "And it was typed in a:", note_editor

#exmaple with more arguments
from sys import argv 

script, apples, oranges, grapes, melons, arguments = argv

print "This script is called:", script
print "We are going to use it to count:", apples
print "We are also going to count:", oranges
print "We can also count:", grapes
print "And my favorite:", melons 
print "This script also has more:", arguments

#Example with "raw_input"
from sys import argv 

script, Monday, Tuesday, Wednesday = argv 

print "this is going to be script:", script 
print "what day is today?:", Monday
today_is = raw_input ()
print "what day is your favorite day?:", Tuesday 
Favorite_day = raw_input()
print "What day comes after tuesday?:", Wednesday
Day_after_tuesday = raw_input()