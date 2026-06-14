from fintrack.db_storage import save_transaction
from fintrack.db_storage import load_transactions


save_transaction(
    {
        "tipo": "receita",
        "valor": 1000,
        "categoria": "salario",
        "descricao": "teste supabase"
    }
)

print("Transação enviada!")

print(load_transactions())