# x is a variable and we giving it a value with strings, we also set the values for "binary"
#and "do_not" so that they can be used inside the strings.
x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#these lines print my variables, where "x" is a statement and "y" too
print x
print y 

#here we start a sentence and we use a format character to insert a variable and finish the sentence
print "i said: %r." % x 
print "i also said: '%s'." % y 

#we set a value for the variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# using only variables we are able to create a sentence 
print joke_evaluation % hilarious

#assigning a value for the variables
w = "this is the left side of ..."
e = "a string with a right side."

#using the variables to create a sentence
#we need to use the "+" to add the variables and get strings. if it's removed the console won't reconize them
#as variables
print w + e