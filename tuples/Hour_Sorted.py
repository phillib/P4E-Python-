name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    hour = words[5] #Takes the entire time out of list
    hour = hour.split(':')[0] #Splits the hour out of the time '09:00:00'
    
    counts[hour] = counts.get(hour, 0) + 1
    
ordered = counts.items()
ordered.sort()

for key, val in ordered:
    print key, val
    
    
#Finds the hour that each email was sent and creates an ordered distribution.
