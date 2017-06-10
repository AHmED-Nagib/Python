import string


def get_middle(s):
    return s[(len(s) - 1) / 2:len(s) / 2 + 1]


print get_middle('1234567')
print get_middle('12345678')


#########################################
def multiples_of_3_and_5(n):
    sum = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


print  multiples_of_3_and_5(1000), multiples_of_3_and_5


#########################################
def find_nb(m):
    sum = 0
    n = 1
    while sum != m:
        sum += pow(n, 3)
        n += 1
        if sum > m:
            return -1
    return n - 1


print find_nb(24723578342962), 'find_nb'


#########################################

def even_fibonacci(n):
    a = 1
    b = 2
    sum = 2
    while b + a < n:
        a, b = b, b + a
        if b % 2 == 0:
            sum += b

    return sum


print even_fibonacci(4000000), 'even_fibonacci'


#########################################

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1: factors.append(n)
            break
    return max(factors)


print  prime_factors(600851475143), prime_factors


#########################################

def count_bits(n):
    count = ''

    for x in str("{0:b}".format(n)).split('0'):
        count += x
    return len(count)


print count_bits(0)
print count_bits(4)
print count_bits(7)
print count_bits(9)
print count_bits(10)


#########################################
def unique_in_order(iterable):
    final_list = []
    if iterable:
        for index in range(0, len(iterable) - 1):
            if iterable[index] != iterable[index + 1]:
                final_list.append(iterable[index])
        final_list.append(iterable[len(iterable) - 1])
        return final_list
    else:
        return final_list


print unique_in_order('aaaaaab')


#########################################

def sort_array(source_array):
    odd_list = [x for x in source_array if x % 2 != 0]
    odd_list.sort()

    print odd_list
    x = 0
    for index in range(0, len(source_array)):
        if source_array[index] % 2 != 0:
            source_array[index] = odd_list[x]
            x += 1
    return source_array


print sort_array([0, 9, 1, 2, 8, 0, 15, 4, 3, 5])


#########################################
def sum_pairs(ints, s):
    final_pair = []
    last_index = 0
    for num in xrange(0, len(ints)):
        x = ints[num]
        print x, 'x'
        try:
            y = ints[ints.index(s - ints[num], num+1)]
        except:
            print x, 'x 5lt'
            y = 'False'
        if type(y) != str:
            if final_pair:
                if ints.index(s - ints[num]) < last_index:
                    final_pair.pop()
                    final_pair.append([x, y])
                    last_index = ints.index(s - ints[num])

            else:
                final_pair.append([x, y])
                last_index = ints.index(s - ints[num], num+1)
                print last_index, 'last_index'

    return final_pair[0]


print sum_pairs( [1, 4, 8, 7, 3, 15] , 8), 'sum_pairs'


