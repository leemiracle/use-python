"""
leemiracle:lov
collections: 容器数据类型
    namedtuple()：factory function for creating tuple subclasses with named fields
    deque：list-like container with fast appends and pops on either end
    ChainMap：dict-like class for creating a single view of multiple mappings
    Counter：dict subclass for counting hashable objects
    OrderedDict:dict subclass that remembers the order entries were added
    defaultdict:dict subclass that calls a factory function to supply missing values
    UserDict:wrapper around dictionary objects for easier dict subclassing
    UserList:wrapper around list objects for easier list subclassing
    UserString:wrapper around string objects for easier string subclassing
heapq:堆队列算法,比如优先队列算法
    which a[k] <= a[2*k+1] and a[k] <= a[2*k+2]
operator:高效的函数
    a set of efficient functions corresponding to the intrinsic operators of Python.
itertools：迭代器
    Functions creating iterators for efficient looping
"""

# 1.Unpacking a Sequence(序列) into Separate Variables:赋值
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

name, shares, price, (year, mon, day) = data

record = ('Dave', '773-555-1212', '847-555-1212', 'dave@example.com')
name, *phone_number, email,  = record
# *phone_number：['773-555-1212', '847-555-1212']

record = ('ACME', 50, 123.45, (12, 18, 2012))
# _为占位符
name, *_, (*_, year) = record
# year: 2012


# 2.Keeping the Last N Items:最多只保留序列的最后N项
# deque:双端
from collections import deque
q = deque(maxlen=3)
for i in range(0, 6):
    q.append(i)
# q: deque([3, 4, 5], maxlen=3)

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # TODO 为什么要用yield返回值
            yield line, previous_lines
            previous_lines.append(line)


# 3.Finding the Largest or Smallest N Items
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
heap = list(nums)
heapq.heapify(heap)
# heap: [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]


# 4.Implementing a Priority Queue
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('spam'), 4).push(Item('bar'), 5)
q.push(Item('grok'), 1)
q.pop() #Item('bar')

# 5.Mapping Keys to Multiple Values in a Dictionary
from collections import defaultdict
"""
defaultdict(list)等价于
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
"""
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
# d : {'a' : [1, 2, 3],'b' : [4, 5]}

# 6.Keeping Dictionaries in Order
from collections import OrderedDict

# 7.Calculating with Dictionaries
zip() #注意zip函数只能使用一次

# 8.Finding Commonalities in Two Dictionaries
# 字典的key值, 其数据结构就是集合，故能使用集合的操作
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'x': 10,
    'y': 2,
    'w': 3
}

# Find keys in common
a.keys() & b.keys()# { 'x', 'y' }


# 9.Removing Duplicates from a Sequence while Maintaining Order
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            # TODO 为什么要用yield
            yield item
            seen.add(val)
# 10.Determining the Most Frequently Occurring Items in a Sequence
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)


# 11. Sorting a List of Dictionaries by a Common Key Problem
from operator import itemgetter
rows = [
    {'fname':'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname':'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname':'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname':'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))

# 12. Grouping Records Together Based on a Field
from itertools import groupby
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
for i in items:
    print(' ', i)


