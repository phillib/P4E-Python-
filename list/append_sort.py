fname = raw_input("Enter file name: ")
fhand = open(fname)
my_list = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()

    for word in words:
        if word not in my_list:
            my_list.append(word)
    my_list.sort()
            
print my_list


# if a word in the file is not in the list 'my_list', add that word to the list.  When finished, sort the list and print.
