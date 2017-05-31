number_of_apples = 16
number_of_students = 10
apples_per_student = 2
desired_num_apples = number_of_students * apples_per_student
print "I have enough apples? %r" % (number_of_apples >= desired_num_apples)
print "Oh. I need %d more apples" % (desired_num_apples - number_of_apples)

no_apple_students = 3
desired_num_apples_2 = (number_of_students - no_apple_students) * apples_per_student
print "I now have enough apples? %r" % (number_of_apples >= desired_num_apples_2)
print "Oh! I have %d extra" % (number_of_apples - desired_num_apples_2)