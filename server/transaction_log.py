


class TransactionLog(object):
    def __init__(self):
        self.transactions = []

    def add_transaction(self, trans):
        self.transactions.append(trans)
