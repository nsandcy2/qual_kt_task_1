from exceptions import InvalidAmountError

class Account:
    def __init__(self):
        self.__balance = 0.0
        self.__transactions = []

    def _validate_amount(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise InvalidAmountError("Invalid type: Amount must be numeric")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

    def _get_balance(self) -> float:
        return self.__balance

    def _update_balance(self, amount: float):
        self.__balance += amount

    def _add_transaction(self, txn):
        self.__transactions.append(txn)

    def _get_transactions(self):
        return list(self.__transactions) 