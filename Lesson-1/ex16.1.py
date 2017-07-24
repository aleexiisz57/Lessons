from sys import argv

script, filename = argv

print "We are going to erase %r." % filename

print "If you don't want that, hit CTR:-C (^C)."
print "if you do want that, hit RETURN"

raw_input("?")

print "opening the file."

target = open (filename, "w")

print "truncating the file. Goodbye!"

target.truncate()

print "Now I'm ging to ask you for three different lines in 1 command"

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

target.writelines([line1, "\n", line2, "\n", line3])

print "Now we are going to close this file. Thank you"

target.close()
