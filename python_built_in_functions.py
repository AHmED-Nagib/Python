import math

print abs(2)
print abs(-2)
print abs(math.sqrt(2))
##################################
x_any = []
y_any = [1, 2, 3]
print any(x_any), 'any(x_any)'
print any(y_any), 'any(y_any)'
print any(xx > 5 for xx in y_any), 'any(xx > 5 for xx in y_any)'
print any(xx < 5 for xx in y_any), 'any(xx < 5 for xx in y_any)'
##################################
x_any = []
y_any = [1, 2, 3]
print all(x_any), 'all(x_any)'
print all(y_any), 'all(y_any)'
print all(xx > 5 for xx in y_any), 'all(xx > 5 for xx in y_any)'
print all(xx < 5 for xx in y_any), 'all(xx < 5 for xx in y_any)'
##################################
print bin(10), 'bin(10)'
print bin(3), 'bin(10)'
##################################
x_bool = 5
xx_bool = 0
xxx_bool = []
xxxx_bool = [1, 2]
xxxxx_bool = [0, 2]
print bool(x_bool), 'bool(x_bool)'
print bool(xx_bool), 'bool(xx_bool)'
print bool(xxx_bool), 'bool(xxx_bool)'
print bool(xxxx_bool), 'bool(xxxx_bool)'
print bool(xxxxx_bool), 'bool(xxxxx_bool)'
##################################
print chr(97), 'chr(97)'


##################################
class Class1(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def produce(cls):
        return "@class_method"


x_classmethod = Class1.produce()

print x_classmethod, 'x_classmethod'
##################################
x_cmp = 1
y_cmp = 2
z_cmp = 2
print cmp(x_cmp, y_cmp), '(x_cmp, y_cmp)'
print cmp(y_cmp, x_cmp), '(y_cmp, x_cmp)'
print cmp(y_cmp, z_cmp), '(y_cmp, z_cmp)'
##################################
x_dir = dict(x=5)
print dir(x_dir), 'dir(x_dir)'


class TestDir(object):
    h_5 = 5

    def __dir__(self):
        return self.h_5


xx_dir = TestDir
print dir(xx_dir), 'dir(xx_dir)'
##################################
print divmod(5, 2), 'divmod', 5 / 2, 5 % 2
##################################
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons)), 'enumerate'
print list(enumerate(seasons, 1)), 'enumerate start 1'
##################################
x_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print filter(lambda x: x % 2 == 0, x_filter)
##################################
print float('-5'), 'float'


##################################
class ClassX:
    pass


class ClassY(ClassX):
    pass


x = ClassX()
y = ClassY()
print isinstance(x, ClassX), 'is object x an instance of class X (or any subclass)?'

print isinstance(x, ClassY), 'is object x an instance of class Y (or any subclass)?'

print isinstance(y, ClassX), 'is object y an instance of class X (or any subclass)?'

print isinstance(y, ClassY), 'is object y an instance of class Y (or any subclass)?'

print issubclass(ClassX, ClassX), ' is class X a subclass of X (including class X)?'

print issubclass(ClassX, ClassY), ' is class X a subclass of Y (including class Y)?'

print issubclass(ClassY, ClassX), ' is class Y a subclass of X (including class X)?'

print issubclass(ClassY, ClassY), ' is class Y a subclass of Y (including class Y)?'

##################################
x_map = [2, 3, 4]
print map(lambda x: x * x, x_map), 'map'


##################################
class TestMax(object):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)


x_max = TestMax(5)
xx_max = TestMax(15)
xxx_max = TestMax(10)


def get_max(cl1, cl2):
    if cl1.x > cl2.x:
        return cl1.x
    else:
        return cl2.x


list_max = [x_max, xx_max, xxx_max]
print max(list_max, key=lambda x: x.x)  # TODO use writen Function instead of lambda Function
print max(list_max, get_max)  # TODO use writen Function instead of lambda Function

###################################

list_next = [1, 2, 3]

n = (num for num in list_next)  # generator

print next(n), 'next'
print next(n), 'next'

###################################

x_reversed = [1, 2, 3]
print [x for x in x_reversed], 'reversed'

