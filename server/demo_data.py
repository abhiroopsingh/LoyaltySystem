from data import *
import datetime

def add_demo_data(db):
    db.update_business(Business("Flourish And Botts", 0,
        "https://welcometohogwarts.files.wordpress.com/2011/09/flourish_and_blotts_sign2.png"))
    
    db.update_business(Business("Ollivander's", 1,
        "https://ih0.redbubble.net/image.217591848.6824/flat,800x800,075,f.u3.jpg"))

    # customer.
    db.update_user(User(0, "potter", "Harry Potter", "*****"))
    db.update_account(AccountBalance(999, 0,0,0))

    db.update_user(User(7, "granger", "Hermione Granger", "****"))
    db.update_account(AccountBalance(998, 1,7,10))
    db.update_account(AccountBalance(997, 0,7,8))

    tme = int(datetime.datetime.now().strftime('%s'))
    transactions = [
        (0, 7, 2, tme - 60*60*2),
        (0,7, 4, tme - 60*60*1),
        (0, 7, 2, tme)
        ]
    for tdata in transactions:
        db.update_transaction(Transaction(*tdata))

    # shopkeep.
    db.update_user(User(2, "shopkeep", "Shopkeeper", "*****", "*****", 0))


