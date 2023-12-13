import heapq

queue = [(0,"A")]

heapq.heappush(queue, (3,"B"))
heapq.heappush(queue, (1,"D"))
heapq.heappush(queue, (1,"E"))
heapq.heappush(queue, (2,"F"))

smallest = heapq.heappop(queue)
print(smallest)


smallest = heapq.heappop(queue)
print(smallest)


smallest = heapq.heappop(queue)
print(smallest)

smallest = heapq.heappop(queue)
print(smallest)