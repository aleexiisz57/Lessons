#formatter is given a variable
formatter = "%r %r %r %r"
#it prints whats inside the parentheses, and formaatter gives you the raw representation 
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#not sure why the line 12 has double-quotes, i tried adding an extra line and i get an
#error where it can't convert line 13. will look more into it
#(Update: explanation by Brian) 
#It's trying to print the string in a way you can type back into the intepreter, 
#so if you have an ', it tries to quote it in double quotes so it doesn't need to escape it with the \ character to print it out.
print formatter % (
	"i had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"so i said goodnight."
)

#One mistake i made was on line 5 where i wrote "true" instead of "True" and Powershell
#would give me an error

#example
print "%r" % "I have a single quote '"
print "%r" % 'I have a double quote "'
print "%r" % "I have both quotes \" and '"