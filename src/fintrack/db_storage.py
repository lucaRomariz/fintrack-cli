from fintrack.database import get_connection

def save_transaction(transaction):
    conn = get_connection()
    
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (
            tipo,
            valor,
            categoria,
            descricao
        )
        VALUES(%s, %s, %s, %s)
        """,
        (
            transaction["tipo"],
            transaction["valor"],
            transaction["categoria"],
            transaction["descricao"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def load_transactions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            tipo,
            valor,
            categoria,
            descricao,
            data
        FROM transactions
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    transactions = []

    for row in rows:

        transactions.append(
            {
                "tipo": row[0],
                "valor": float(row[1]),
                "categoria": row[2],
                "descricao": row[3],
                "data": str(row[4]),
            }
        )

    return transactions