#setting up the value for a variable but we use a escape sequence to tab the sentence.
tabby_cat = "\tI'm tabbed in."
# we use \non to start a new string in a different line.
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

#here we make a list where we use the escape sequences to tab the items and list them.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
#printing variables with the escape sequences represented.
print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#Escape Sequences

#Escape 	What it does.
#\\         Backlash (\)
#\'			Single-quote(')
#\"			Double-quote(")
#\a			ASCII bell (BEL)
#\b 		ASCII backspace (BS)
#\f 		ASCII formfeed (FF)
#\n 		ASCII linefeed (LF)
#\N{name} 	Character named name in the unicode database (Unicode only)
#\r 		ASCII carriage return (CR)
#\t 		ASCII horizontal tab (TAB)
#\uxxxx		Character with 16-bit hex value xxxx (Unicode only)
#\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v 		ASCII vertical tab (VT)
#\ooo		Character with octal value oo 
#\xhh 		Character with hex value hh

#Not sue what it does, It created a spinning stick that woudn't let me
#type back into the Powershell until i restarted.
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
		
