# linear complexity
def add_digits(s):
    """
    >>> add_digits('12')
    3
    >>> add_digits('17')
    8
    >>> add_digits('13')
    4
    """
    val = 0
    for c in s:
        val += int(c)
    return val

def fact_iter(n):
    """
    1. number of times around loop is n
    2. number of operations inside loop is a constant
    3. overall just O(n)

    >>> fact_iter(5)
    120
    >>> fact_iter(12)
    479001600
    >>> fact_iter(10)
    3628800
    >>> fact_iter(16)
    20922789888000
    >>> fact_iter(4)
    24
    """
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

# Algorithm complexity

def isSubset(L1, L2):
    """
    >>> isSubset([1,2,3], [2,3,4])
    False
    >>> isSubset([1,2,3], [2,3,1])
    True
    >>> isSubset([2,4,3], [2,3,4])
    True
    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

def search(L, e):
	"""
	1. must only look until reach a number greater than e
	2. O(len(L)) for the loop * O(1) to test if e == L[i]
	3. Overall complexity is O(n) - where n is the len(L)

    >>> search([1,2,3,4], 5)
    False
    >>> search([1,2,3,4], 6)
    False
    >>> search([1,2,3,4], 2)
    True
	"""
	for i in range(len(L)):
		if L[i] == e:
			return True
			"""You can return the value found return e """
		if L[i] > e:
			return False
	return False

def bisect_search1(L, e):
	"""where L is list and e is element
    >>> bisect_search1([], 1)
    False
    >>> bisect_search1([2], 1)
    False
    >>> bisect_search1([1], 1)
    True
    """
	if L == []:
		return False
	elif len(L) == 1:
		return L[0] == e
	else:
		half = len(L) // 2
		if L(half) > e:
			return bisect_search1( L[:half], e)
		else:
			return bisect_search1( L[half:], e)

test_list = [1, 2, 3, 5, 7, 9, 18, 27]


def bisect_search2(L, e):
    """
    >>> bisect_search2([2,3,4,5, 'andile', 'mzie'], 2)
    True
    >>> bisect_search2([2,3,4,5, 'andile', 'mzie'], 1)
    False
    >>> bisect_search2([2,3,4,5], 5)
    True
    """
    def bisect_search_helper_fn(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search for
                return False
            else:
                return bisect_search_helper_fn(L, e, low, mid - 1)
        else:
            return bisect_search_helper_fn(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper_fn(L, e, 0, len(L) - 1)

test_list = [1, 2, 3, 5, 7, 9, 18, 27]

def intToStr(i):
    """
    What we know.

    1. Only have to look at the loop as there are  no function calls
    2. Within while loop, constant number of steps
    3. How many times through loop?
        i. how many times can one divide i by 10
        ii. O(log(i)), log base 10 for the size of i
        Nugget: It is linear in the number of digits in n, but log in the size of n and since we decided to measure this in the size of the input it is logarithmic

    >>> intToStr(12)
    '12'
    >>> intToStr(1)
    '1'
    >>> intToStr(9)
    '9'
    """
    digits = '0123456789'
    if i == 0:
        return '0'
    res = ''
    while i > 0:
        res = digits[i % 10] + res
        i = i // 10
    return res

def intersect(L1, L2):
    """
    1. first nested loop takes len(L1)*len(L2) steps
    2. second loop takes at most len(L1) steps
    3. Latter term overwhelmed by form term
    4. O(len(L1)*len(L2))
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res =  []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

def gen_subsets(L):
    """
    Exponential Complexity

    1. it's prevalent to think about size of smaller
    2. Remember that for a set of size K there are pow(2, k) cases
    3. To solve this we need something like pow(2, n-1) + pow(2, n-2) + ... + pow(2, 0)

    >>> gen_subsets([1,2])
    [[], [1], [2], [1, 2]]
    >>> gen_subsets([1,3])
    [[], [1], [3], [1, 3]]
    >>> gen_subsets([1,2,3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    res = [] # empty list
    if len(L) == 0:
        return [[]] # list of an empty list
    smaller = gen_subsets(L[:-1]) # recursive return all subsets without last element
    extra = L[-1:] # create a list of just the last element
    new = [] # again, empty list
    for small in smaller:
        new.append(small + extra) # for all smaller solutions, add one with last element
    return smaller + new

def search_for_elmt(L, e):
    """
    >>> search_for_elmt([1,2,3,4], 2)
    True
    >>> search_for_elmt([2,4,6,8], 3)
    False
    >>> search_for_elmt(list(range(1**2, 10)), 4)
    True
    """
    for i in L:
        if i == e:
            return True
    return False

def h(n):
	"""assumes n an int >= 0

    >>> h(1)
    1
    >>> h(2)
    2
    >>> h(3)
    3
    >>> h(4)
    4
    """
	answer = 0
	s = str(n)
	for c in s:
		answer += int(c)
	return answer


def g(n):
	"""assume n >= 0

    1. Computes n ** 2 very inefficiently
    2. Whenk dealing with nested loops, look at the ranges
    3. Nested loops, each iterating n times

    >>> g(3)
    9
    >>> g(5)
    25
    >>> g(7)
    49
    """
	x = 0
	for i in range(n):
		for j in range(n):
			x += 1
	return x

def c_to_f(c):
    """
    >>> c_to_f(38)
    100.4
    >>> c_to_f(32)
    89.6
    >>> c_to_f(5000)
    9032.0
    >>> c_to_f(100)
    212.0
    """
    return c * 9.0/5 + 32

def my_sum(x):
    """
    >>> my_sum(4)
    10
    >>> my_sum(7)
    28
    >>> my_sum(2)
    3
    >>> my_sum(100)
    5050
    """
    total = 0
    for i in range(x + 1):
        total += i
    return total

def isPal(x):
    """
    >>> isPal(['a', 'b'])
    ['a', 'b'] ['a', 'b']
    ['b', 'a'] ['a', 'b']
    False
    >>> isPal(['a', 'b', 'a'])
    ['a', 'b', 'a'] ['a', 'b', 'a']
    ['a', 'b', 'a'] ['a', 'b', 'a']
    True
    """
    assert type(x) == list, 'not a list' # assert to make sure x is a list
    tmp = x[:] # make a copy instead of referencing to the whole object
    print(tmp, x) # print before reversing
    tmp.reverse()
    print(tmp, x) # print after reversing
    if tmp == x:
        return True
    else:
        return False

def silly(n):
    """
    >>> silly(2)
    Enter element: a
    Enter element: b
    ['a', 'b'] ['a', 'b']
    ['b', 'a'] ['a', 'b']
    No
    >>> silly(3)
    Enter element: t
    Enter element: a
    Enter element: t
    ['t', 'a', 't'] ['t', 'a', 't']
    ['t', 'a', 't'] ['t', 'a', 't']
    Yes
    """
    res = []
    for i in range(n):
        elmt = input('Enter element: ')
        res.append(elmt)
    if isPal(res):
        print('Yes')
    else:
        print('No')

def get_stats(class_list):
    new_stats = []
    for elmt in class_list:
        new_stats.append([elmt[0], elmt[1], avg(elmt[1])])
    return new_stats

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
                [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
                [['captain', 'america'], [8.0, 10.0, 96.0]],
                [['deadpool'],[]]]

# def avg(grades):
#     """Assertions; an example of good defensive programming
#
#     >>> avg([68, 89, 96, 88, 75])
#     83.2
#     >>> avg([68, 50, 91, 80, 65])
#     70.8
#     >>> avg([49, 60, 81, 97, 55])
#     68.4
#     """
#     assert not len(grades) == 0, 'no grades data'
#     return sum(grades) / len(grades)

# def avg(grades):
#     return sum(grades) / len(grades)

# def avg(grades):
#     try:
#         return sum(grades) / len(grades)
#     except ZeroDivisionError:
#         print('no grades data')

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0

def get_ratios(L1, L2):
    """Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[1]

    >>> get_ratios([1, 2, 3, 4], [2, 4, 6, 8])
    [0.5, 0.5, 0.5, 0.5]
    >>> get_ratios([4, 9, 10, 7], [3, 2, 9, 11])
    [1.3333333333333333, 4.5, 1.1111111111111112, 0.6363636363636364]
    """

    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError('get_ratios called with bad args')
    return ratios
