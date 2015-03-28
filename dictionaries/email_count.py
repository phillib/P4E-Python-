name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

bigcount = None
bigemail = None

for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    
    counts[email] = counts.get(email, 0) + 1
    
for email,count in counts.items():
    if bigcount is None or count > bigcount:
    	bigemail = email
    	bigcount = count
    


print bigemail, bigcount
