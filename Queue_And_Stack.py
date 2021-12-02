import queue

numberlist = [x for x in range(301)]

numberlist.pop()
print(numberlist)

import queue

# Queue is created as an object 'L'
L = queue.Queue(maxsize=10)

y = 0
for x in range(10):
    L.put(y)
    y += 1

for x in range(10):
    L.get()
    print(L.get())
