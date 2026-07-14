class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    
    def balanceElements(self):
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def balanceLength(self):
        if len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def addNum(self, num: int) -> None:
        # add the num to small everytime
        heapq.heappush(self.small, -1 * num)

        # balance element
        self.balanceElements()

        # balance length
        self.balanceLength()
    

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        
        