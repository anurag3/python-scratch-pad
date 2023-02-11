class BrowserHistory_DoublyLinkedList:
    """
    You have a browser of one tab where you start on the homepage and you can visit another url,
    get back in the history number of steps or move forward in the history number of steps.

    Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and
        steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and
    steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
    """

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


class BrowserHistory_Stack:
    def __init__(self, homepage: str):
        self.current_position = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.current_position + 2:
            self.history.append(url)
        else:
            self.history[self.current_position + 1] = url
        self.current_position += 1
        self.len = self.current_position + 1

    def back(self, steps: int) -> str:
        # We are using max operation to ensure pointer >= 0
        # to avoid pointer from going out of lower bounds
        self.current_position = max(self.current_position - steps, 0)
        return self.history[self.current_position]

    def forward(self, steps: int) -> str:
        # We are using max operation to ensure pointer <= 0
        # to avoid pointer from going out of upper bounds
        self.current_position = min(self.current_position + steps, self.len - 1)
        return self.history[self.current_position]
