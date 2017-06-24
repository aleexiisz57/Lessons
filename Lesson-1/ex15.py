#What this line does is calling the name of the .txt file and inserting it into a string
from sys import argv
#This lines gives a value to scrip and file name so that they can be called from "argv"
script, filename = argv
#What this line does is giving an action to the variable "txt" that tells it 
#to open a text file letting you type the name of the file and opening its content.
txt = open(filename)
#this line calls the name of the file that you input into the console.
print "Here's your file %r:" % filename
#this line prints out whatever is inside the .txt file for display
print txt.read()
#this line prints out a string
print "Type the filename again:"
#this line gives a variable that equals a raw input where you input the file name. 
file_again = raw_input("> ")
#this line will open the .txt file again.
txt_again = open(file_again)
#this line will display the content inside the .txt file again.
print txt_again.read()