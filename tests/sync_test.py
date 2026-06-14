from fintrack.sync_service import sync_transactions

total = sync_transactions()

print(f"{total} transações sincronizadas.")