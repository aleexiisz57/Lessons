number_of_apples = 16
number_of_students = 10
apples_per_student = 2
desired_num_apples = number_of_students * apples_per_student
no_apple_students = 3
desired_num_apples_2 = (number_of_students - no_apple_students) * apples_per_student
num_of_oj = 23
number_of_students_2 = 16 
 
print "If 10 students want apples and i only have 16 apples. How many apples do i need so everyone can have two? %r" % (desired_num_apples)
print "I have enough apples? %r" % (number_of_apples >= desired_num_apples)
print "How many more apples do we need so that everyone can have 2?"
print (number_of_students * apples_per_student) - number_of_apples 
print "three kids decided they didnt want apples. How many apples do we have extra? %r" % (no_apple_students * apples_per_student)
print "there is also 32 O.J cartons, and and 16 students, would they be able to have two juices? %r" % ( num_of_oj >= number_of_students_2)
