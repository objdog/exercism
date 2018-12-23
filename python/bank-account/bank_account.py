import threading
threadLock = threading.Lock()
class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.status = False

    def get_balance(self):
        if self.status == True:
            return self.balance
        else:
            raise ValueError("That is not an open account.")

    def open(self):
        if self.status == False:
            self.status = True
        else:
            raise ValueError("The account is already open.")

    def deposit(self, amount):
        if self.status == True and amount > 0:
            threadLock.acquire()
            try:
                self.balance += amount
            finally:
                threadLock.release()
        else:
            raise ValueError("A problem occured with your deposit. No deposit was made.")

    def withdraw(self, amount):
        if self.status == True and amount > 0 and amount <= self.balance:
            threadLock.acquire()
            try:
                self.balance -= amount
            finally:
                threadLock.release()
        else:
            raise ValueError("A problem occured with your withdrawl. No withdrawl was made.")

    def close(self):
        if self.status == True:
            self.balance = 0
            self.status = False
        else:
            raise ValueError("The account is already closed.")
