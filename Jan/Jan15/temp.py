# print(sorted("hello"))
# print(tuple(sorted('hello')))

from collections import Counter

count = Counter([1,1,1,2,3,4,5,5,5,6,7,7,7,7,7])

print(type(count))

print(count)

for i, n in count.items():
    print(i, n)