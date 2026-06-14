from fintrack import storage
from fintrack.db_storage import save_transaction


def sync_transactions():

    transactions = storage.load_transactions()

    total = 0

    for transaction in transactions:

        save_transaction(transaction)

        total += 1

    return total

