from queue import Queue

q = Queue(maxsize=3)

#Enqueue

q.put(1)
q.put("gokul")
q.put("25")


#To check if it is full

print(q.full())
#Dequeue

a = q.get()
b = q.get()
print(a)
print(b)

#Front

print(q.queue[0])

#Is empty

print(q.empty())


