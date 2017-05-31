#formatter is given a variable
formatter = "%r %r %r %r"
#it prints whats inside the parentheses, and formaatter gives you the raw representation 
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#not sure why the line 12 has double-quotes, i tried adding an extra line and i get an
#error where it can't convert line 13. will look more into it
print formatter % (
	"i had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"hello there.",
	"so i said goodnight."
)

#One mistake i made was on line 5 where i wrote "true" instead of "True" and Powershell
#would give me an error