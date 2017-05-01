#########################################
x = 5
if x < 5:
    print "<"
elif x == 5:
    print "="
else:
    print ">"
#########################################

tuple_list = [(1, 2), (3, 4)]
int_list = [1, 2, 3]
for (x, y) in tuple_list:
    print x, x * y

print range(0, 11, 2)  # for(x=0,x<11,+2)

a = {'one': 1, 'two': 2, 'three': 3}
for x in a.iteritems():
    print x
for x, y in a.iteritems():
    print x

#########################################
x = 1
while x < 10:
    if x != 3 and x != 6:
        print x
        x += 1
    elif x == 3:
        print x
        print "i will just continue and go dir to the top "
        x += 1
        continue
    elif x == 6:
        print "i will breake"
        break

    print "end of this round "
