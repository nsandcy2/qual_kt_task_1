from account import Account
from transaction import Transaction
from exceptions import InsufficientBalanceError

class UserAccount(Account):
    def __init__(self,name: str = "User"):
        super().__init__()
        self.name = name

    total_transactions = 0

    def credit(self, amount: float):

        self._validate_amount(amount)
       

        txn = Transaction("credit", amount)
        self._update_balance(amount)
        self._add_transaction(txn)

        UserAccount.total_transactions += 1

    def debit(self, amount: float):

        self._validate_amount(amount)

        if amount > self._get_balance():
            raise InsufficientBalanceError("Insufficient balance")

       

        txn = Transaction("debit", amount)
        self._update_balance(-amount)
        self._add_transaction(txn)

        UserAccount.total_transactions += 1

    def get_balance(self) -> float:
        return self._get_balance()

    def get_summary(self):
        return {
            "balance": self.get_balance(),
            "transactions": [str(txn) for txn in self._get_transactions()]
        }

    def __str__(self):
        return f"UserAccount(name={self.name}, balance=₹{self.get_balance()})"