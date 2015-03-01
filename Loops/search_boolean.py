found = False
print 'Before', found
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print found, value
print 'After', found

# This loop will loop through the list and return True if the object assigned to 'value' is within it.
# for example, will print "After, True" if the list contains the number 3.
# Helpful for determing if a value or string is contained in a very large data set.
