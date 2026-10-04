class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)

    def visit(self, url: str) -> None:
        new_page = Node(url, self.homepage)
        self.homepage.next = new_page
        self.homepage = new_page

    def back(self, steps: int) -> str:
        while self.homepage.prev and steps > 0:
            self.homepage = self.homepage.prev
            steps -= 1
        
        return self.homepage.val

    def forward(self, steps: int) -> str:
        while self.homepage.next and steps > 0:
            self.homepage = self.homepage.next
            steps -= 1
        
        return self.homepage.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)