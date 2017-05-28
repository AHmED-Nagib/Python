from collections import Counter
from collections import defaultdict
import datetime
# import bdb
import timeit

list1 = [1, 2, 3]
list2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
list2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
list3 = [(1, 2, 3), (1, 2, 3), (1, 2, 2)]
print Counter(list1)
# Counter(list2) that will give error cuz [list] is not hashable type "it is mutable"
print Counter(list3)
print Counter(list3).most_common()[0], '-> most_common()'
print Counter(list3).most_common()[-1], '-> lest_common()'
print [x for x in Counter('abababccca').elements()], '-> elements()'
##############################
d = defaultdict(lambda: 1)
d['a']
d['b'] = 2
print d
for x, y in d.iteritems():
    print y
##############################
time1 = datetime.time(14, 9, 30)
time2 = datetime.datetime(2017, 4, 13, 14, 21, 30)
time3 = datetime.datetime(2016, 3, 12, 14, 21, 30)
time4 = time2 - time3
time5 = datetime.timedelta(days=20)
print time4.days
print time1
print time2
print time4
# bdb.set_trace()
print time2 - time5
print time2 - (time2 - time3)
print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print timeit.timeit('"-".join(map(str, range(100)))', number=10000)
