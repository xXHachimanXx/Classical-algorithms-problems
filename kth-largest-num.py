class KthLargestNumberInStream:
   def __init__(self, input=[], k=0):
      self.heap = []
      self.size = 0
      self.k = k
      
      for num in input:
         self.add(num)

   def heap_push(self, num):
      self.heap.append(num)
      self.size += 1

      curr = self.size-1

      while curr > 0 and self.heap[curr] < self.heap[(curr-1)//2]:
         self.heap[(curr-1)//2], self.heap[curr] = self.heap[curr], self.heap[(curr-1)//2]
         curr = (curr-1)//2

   def heap_pop(self):
      popped = self.heap[0] # pop root
      self.size -= 1
      self.heap[0] = self.heap[self.size - 1] # promove last
      curr = 0

      while 2*curr+1 < self.size:
         if 2*curr+2 == self.size:
            child = 2*curr+1
         else:
            child = 2*curr+1 if self.heap[2*curr+1] < self.heap[2*curr+2] else 2*curr+2

         if self.heap[child] < self.heap[curr]:
            self.heap[curr], self.heap[child] = self.heap[child], self.heap[curr]
            curr = child
         else:
            break

      self.heap.pop(self.size-1)

      return popped


   def add(self, num):
      self.heap_push(num)

      if self.size > self.k:
         self.heap_pop()

      return self.heap[0]


def main():
   kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
   assert kthLargestNumber.add(6) == 5
   assert kthLargestNumber.add(13) == 6
   assert kthLargestNumber.add(4) == 6
   assert kthLargestNumber.add(9) == 9

main()
