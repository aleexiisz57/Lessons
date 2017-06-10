#here we print a question and then we get a input action where you can type something.
print "How old are you?",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

#Here we use the format character "%r" to input the variables into the string.
print "So, you're %r old, %r tall and %r heavy." % ( age, height, weight)