largest = None # "None" tells python that no data has been entered yet.
smallest = None
while True: # begin infinite loop
    num = raw_input("Enter a number: ")
    if num == "done" : break # if user enters "done", exit loop and calculate large/small
    if len(num) < 1: break  # if user presses enter with no input, exit loop and calculate large/small
        
    try:
        inp = int(num) # check to see if user entry is a number
    except:
        print "Invalid input" # if user enters something other than a number or "done", print error.
        continue # If user entered "invalid input", go back to the top of the loop.  Do not run code below.

    if smallest is None: # for first iteration of loop, assigns the first user entry to the value "smallest"
        smallest = num
    elif num < smallest: # if user entry is smaller than previous number, assign new number to variable "smallest"
        smallest = num
        
    if largest is None: # for first iteration of loop, assigns the first user entry to the value "largest"
        largest = num
    elif num > largest: # if user entry is larger than previous number, assign new number to variable "largest"
        largest = num

print "Maximum is", largest
print "Minimum is", smallest

# Find the largest and smallest of the numbers entered by the user.
