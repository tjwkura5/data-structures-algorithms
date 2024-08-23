# You have a browser of one tab where you start on the homepage and you can 
# visit another url, get back in the history number of steps or move forward in 
# the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. 
# If you can only return x steps in the history and steps > x, you will return only x steps.
# Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. 
# If you can only forward x steps in the history and steps > x, you will forward only x steps. 
# Return the current url after forwarding in history at most steps.

class Site:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, url):
        site = Site(url)
        self.cur = site
        self.size = 1

    def visit(self, url):
        site = Site(url)
        self.cur.next = site
        site.prev = self.cur
        self.cur = site

        self.size +=1 
    
    def back(self, steps):
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -=1
        return self.cur.url

    def forward(self, steps):
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -=1
        return self.cur.url

