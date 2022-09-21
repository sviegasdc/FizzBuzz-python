"""print 1 .. 100
print"Fizz" if divisible by 3
print "Buzz" if divisible by 5
print "FizzBuzz" if divisible by 3 and 5.
"""
for i in range (1,101):
    if (i%3 == 0 and i%5 == 0):
        print ("FizzBuzz")
    elif (i%3 == 0):
       print ("Fizz")
    elif (i%5 == 0):
        print ("Buzz")
    else:
        print (i)
    