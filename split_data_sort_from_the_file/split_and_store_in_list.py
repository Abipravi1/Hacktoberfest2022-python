fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    for i in line.split():
        if i  not in lst: 
            lst.append(i)
lst.sort()
print(lst)
