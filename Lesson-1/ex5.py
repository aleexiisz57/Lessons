my_name = 'ZED A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches 
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "his teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d i get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#format symbol | Conversion
#%c	character
#%s	string conversion via str() prior to formatting
#%i	signed decimal integer
#%d	signed decimal integer
#%u	unsigned decimal integer
#%o	octal integer
#%x	hexadecimal integer (lowercase letters)
#%X	hexadecimal integer (UPPERcase letters)
#%e	exponential notation (with lowercase 'e')
#%E	exponential notation (with UPPERcase 'E')
#%f	floating point real number
#%g	the shorter of %f and %e
#%G	the shorter of %f and %E