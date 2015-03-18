count = 0
total = 0


fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue

    else:
        pos = line.find(':')
        num = float(line[pos + 1:])
        total = total + num
        count = count + 1
        
average = total / count
print "Average spam confidence:", average

# Looks for all occurences of the line X-DSPAM, strips the number out, and averages all of the numbers.
