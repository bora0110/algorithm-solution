a = 'a'
b = 'b'
target = ''
parent = 'ab'


print('a={}, b={}, target={}, parent={}'.format(a, b, target, parent))

target = b if a == parent else a

print('a={}, b={}, target={}, parent={}'.format(a, b, target, parent))



answer = [ i for i in range (5 - 1, -1, -1)]
print(answer)

print(abs(len([1,2]) - len([1,2,3])))

num = 4
print(list(str(num)))
print('===========')
lst = ['0', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1']
print(lst)
idx2 = ''.join(lst).rfind('0')
idx3 = ''.join(lst).find('1', idx2)
print('{} , {}'.format(idx2,idx3))
lst[idx2], lst[idx3] = lst[idx3], lst[idx2]
print(lst)

print('===========')
from collections import deque

lst = [1,2,3,4,5]
q = deque(lst)
# q.reverse()
# q.reverse()
print(q)

del lst[0:100]
print(lst)

print('===========')
x= 0
w = ')'
x = 1 if w=="(" else 2 if w==")" else x
print(x)

print('===========')
for a in range(2):
    print(a)