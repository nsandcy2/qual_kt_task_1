from datetime import datetime
import uuid

class Transaction:
    def __init__(self, txn_type: str, amount: float):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.transaction_type = txn_type
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"[{self.timestamp}] "
            f"{self.transaction_type.upper()} "
            f"₹{self.amount} (ID: {self.id})"
        )