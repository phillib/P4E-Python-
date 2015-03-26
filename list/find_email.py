fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fhand = open(fname)
count = 0

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words == []: continue # accounts for blank lines
    if 'From:' in words: continue
    if words[0] != 'From': continue
    count = count + 1
    print words[1]
    
print "There were", count, "lines in the file with From as the first word"
