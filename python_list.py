l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l1.append('6')
print l1, "append"
l1.extend(l2)
print l1, "extend"
l1.insert(len(l1), l2)
print l1, "insert"
l1.remove(l2)
print l1, "remove"
l1.pop(5)
print l1, "pop"
index1 = l1.index(10)
print index1, "index"
count1 = l1.count(2)
print count1, "count"
l1.sort()
print l1, "sort"
l1.reverse()
print l1, "reverse"
del l1[0:5]
print l1, "del"
print enumerate(l1)
for x,y in enumerate(l1):
    print x,y

