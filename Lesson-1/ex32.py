the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of  for-loop goes through a list
for number in the_count:
	print "this is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we dont know what's in it
for i in change:
	print "I got %r" % i 
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

# example of range function by "http://pythoncentral.io/pythons-range-function-explained/"
# one parameter
for i in range(5):
	print(i)
	
0
1
2
3
4
# two parameters
for i in range(3, 6):
	print(i)

3
4
5
#three parameters 
for i in range(4, 10, 2):
	print(i)
	
4	
6	
8
# going backwards
for i in range(0, -10, -2):
	print(i)

0
-2
-4
-6
-8