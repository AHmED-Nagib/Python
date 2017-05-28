a = {'one': 1, 'two': 2, 'three': 3}
b = dict(one=1, two=2, three=3)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print len(a), 'len'
del b['one']
print b, 'del(key)'
c.clear()
print c, 'use clear()'
f = dict.fromkeys(['a', 'b', 'c'], [1, 2, 3])
print f, "fromkeys"
print a.items(), 'items()'
print a.iteritems(), 'iteritems()'
print a.setdefault('four', 4), 'the return of setdefault()'
print a
print a.setdefault('three', 31), 'the return of setdefault()'
print a
print b, ' b before update'
b.update(a)
print b, 'b after update'

# dict comprehension
print {'key' + str(x + 1): x + 1 for x in range(11)}
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print {k: v for k, v in zip(list1, list2)}


