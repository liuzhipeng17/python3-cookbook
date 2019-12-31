#1 创建Heapq的方法1
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap,3)
heapq.heappush(heap,15)
heapq.heappush(heap,-5)
heapq.heappush(heap,-9)
heapq.heappush(heap,42)

#2 创建heapq的方法2

nums = [1, 3, 15, -5, -9, 42]
heapq.heapify(nums)
nums[0] # nums就是一个堆了

#3 堆数据结构的重要特征

heap[0]永远是最小的元素。并且剩余的元素可以通过heapq.heappop()方法得到。
heappop()会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素。

#4 如果想要查找最小的3个元素，可以这样做：
>>>heapq.heappop(heap)
>>>heapq.heappop(heap)
>>>heapq.heappop(heap)

#5 nlargest(n, iterable[,key])  nsmallest(n ,iterable[,key])

比如，key=str.lower, 等效sorted(iterable, key=str.lower, reverse=True)[:n]

如果N=1, 采用min(), max()
