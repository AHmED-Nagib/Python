import string


def first_letters(s):
    print string.join([x[0] for x in s.split(' ')])


first_letters('Ahmed Nagib')


######################################
def is_prime(num):
    for x in range(2, num):
        if num % 2 == 0:
            return "not prime"
    return "prime"


print is_prime(10)
print is_prime(11)


######################################

class Shape1(object):
    def __init__(self):
        print "Shape1 is Created"
        self.height1 = 0

    def fn(self):
        print "Shape1"
        self.height1 = 5


class Shape2(object):
    def __init__(self):
        print "Shape2 is Created"
        self.height2 = 0

    def fn(self):
        print "Shape2"
        self.height2 = 5


class Shape3(Shape1, Shape2):
    pass


shape1 = Shape3()
print shape1.fn()


def fun_input():
    x = raw_input("please say something")
    print x
