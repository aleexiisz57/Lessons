from sys import argv

script, filename = argv
#What this line does is giving you the name of the file you typed in
print "We're going to erase %r." % filename
#This is a line with strings thats just telling you the commands and options
#so that you can delete or keep the file.
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#This line is the input where you type if you want the file erased or you want to keep it
raw_input("?")
#This string is telling you that the file is going to be opened.
print "Opening the file..."
#This line actually opens the file.
target = open (filename, "w")
#This is a string telling you the file is going to be deleted
print "truncating the file. Goodbye!"
#This line is the actual file being deleted
target.truncate()
#This string is asking you to tyoe 3 different lines
print "Now I'm going to ask you for three lines."
#This is the first line that will get written into the file.
line1 = raw_input("line1: ")
#This is the second line that will get written into the file
line2 = raw_input("line2: ")
#This is the third line that will get written into the file
line3 = raw_input("line3: ")
#This string is telling you that whatever you wrote on the other lines i
print "I'm going to write these to the file."
#This line writes the raw_input for line 23
target.write(line1)
#This line creates a new line in the .txt document
target.write("\n")
#This line wrtites the raw_input for line 25
target.write(line2)
#This line creates a new line in the .txt document
target.write("\n")
#This line writes the raw_input for line 27
target.write(line3)
#This line creates a new line the the .txt document
target.write("\n")
#This line is a string telling you what you have just done.
print "And finally we close it."
#This line closes the document that you open and wrote the lines too.
target.close()
