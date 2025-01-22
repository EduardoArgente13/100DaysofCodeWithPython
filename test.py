class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        
    def is_valid_account(self, account):
        return 1 <= account <= len(self.balance)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if self.is_valid_account(account1) and self.is_valid_account(account2) and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.is_valid_account(account):
            self.balance[account - 1] += money
            return True
        else:
            return False
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.is_valid_account(account) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False
        


# Your Bank object will be instantiated and called as such:
bank = Bank([10, 100, 20, 50, 30])

print(bank.withdraw(3, 10))  # true
print(bank.transfer(5, 1, 20))  # true
print(bank.deposit(5, 20))  # true
print(bank.transfer(3, 4, 15))  # false
print(bank.withdraw(10, 50))  # false