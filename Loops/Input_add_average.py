count = 0
total = 0
while True:
    inp = raw_input("Enter a number: ")
    
    # Handle the edge cases
    if inp == "done": break
    if len(inp) < 1: break  # Check for an empty line
        
    # Do the work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue # This will prompt raw input again without running the code below
    count = count + 1
    total = total + num
    print num, total, count
print "Average:", total / count

# Prompts the user to enter numbers they want to add together and calculate an average for.
# Once all numbers are entered, user types "done" or presses enter to calculate.
# If something other than "done" or an integer is entered, "Invalid input" will print
# and the user will be promped to enter another number.
