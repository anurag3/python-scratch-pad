class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # popleft is the same operation as removing from left side
        #   so to maintain the logic if we have [1,2,3] and we want to remove "3"
        #   we will be poping from left and putting the values back till the
        #   length of queue. So we will pop "1" and "2" as we normally would and
        #   append them back in the queue so we would have [3,1,2] and now we will
        #   pop again and return that value
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
