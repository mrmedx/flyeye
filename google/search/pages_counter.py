#@class pages counter
class VisitedPagesCounter:
    def __init__(self):
        self.VISITED=0

    def back_to_zero(self):
        self.VISITED=0

    def get(self):
        return self.VISITED
    
    def get_str(self):
        return str(self.VISITED)
    
    def next(self, value=10):#go to VISITED+=value pages
        self.VISITED+=value

    def prev(self,value=10):#go to VISITED-=value pages
        self.VISITED-=value

#@VISITED_PAGES count the visited search result pages
VISITED_PAGES = VisitedPagesCounter()