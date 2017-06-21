from sys import argv

script, user_name = argv 
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) 

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# example with different variables and more arguments

from sys import argv 

script, user_name, country = argv
prompt = '- '

print "Hello there %s, my name is %s script. You are from %s." % (user_name, script, country)

print "I would like to ask you some questions about your country."
print "What's the type of music they mostly listen to?"
music = raw_input(prompt)

print "What is their favorite food in %s?" % country
food = raw_input(prompt)

print "And what is their regional fruit?"
fruit = raw_input(prompt)

print """
%s you are from %s,
where they like to listen to %r,
their favorite food is %r
and their regional fruit is %r""" % (user_name, country, music, food, fruit)