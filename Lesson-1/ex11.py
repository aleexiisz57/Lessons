#here we print a question and then we get a input action where you can type something.
print "How old are you?",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

#Here we use the format character "%r" to input the variables into the string.
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
	
#What "raw_input" does is it gets input from the user and returns the data input by the user in a string.

#Example_1
oranges  = raw_input("How many oranges did you count? ")
print "I counted %s oranges." % oranges

#Example_2
print "What country are you from?",
country = raw_input()
print "What's your favorite color?"
color = raw_input()
print "What's your favorite activity?",
activity = raw_input()

print "Your country is %r, your favorite color is %r and your favorite activity is %r." % (
	country, color, activity)