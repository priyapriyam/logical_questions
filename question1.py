list1 = [1, 342, 75, 23, 98,0,7]
list2 = [75, 23, 98, 12, 78, 10, 1]
i=0
j=0
new=[]
while i < len(list1):
    while j <len(list2):
        if (list1[i]) in (list2):
            new.append(list1[i])
        i=i+1
        j=j+1
print new