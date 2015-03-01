smallest = None # tells python a number has not been defined yet.
print 'Before'
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value # sets value on first iteration through the loop.
    elif value < smallest:
        smallest = value # if number is smaller than previous, it replaces "smallest".
    print smallest, value
print "After", smallest


# finds the smallest value in a list of numbers
