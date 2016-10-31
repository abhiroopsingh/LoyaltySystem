from data import *

def add_demo_data(db):
    db.update_business(Business("Flourish And Botts", 0))

    # customer.
    db.update_user(User(0, "potter", "Harry Potter", "*****"))
    db.update_account(AccountBalance(999, 0,0,0))
