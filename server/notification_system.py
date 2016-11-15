from collections import defaultdict

class NotificationServer(object):
    def __init__(self):
        self.waiting_responses = defaultdict(list)

    def add_waiter(self,idn, wait_func):
        self.waiting_responses[idn].append(wait_func)

    def notify(self,idn, obj):
        for itm in self.waiting_responses[idn]:
            itm(obj)
        self.waiting_responses[obj] = []
    
