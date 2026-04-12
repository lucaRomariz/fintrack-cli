"""Regras de negócio do gestor financeiro.

Este módulo não sabe COMO os dados são salvos — ele delega isso ao storage.
Se amanhã trocarmos JSON por banco de dados, só o storage muda.
"""

from datetime import datetime
from pathlib import Path

from fintrack import storage

TIPOS_VALIDOS = {"receita", "despesa"}


class FinancialManager:
    """Gerencia transações financeiras: adiciona, lista, resume e agrupa."""

    def __init__(self, filepath: Path = storage.DEFAULT_DATA_FILE):
        # Recebe o caminho do arquivo como parâmetro.
        # Isso permite que os testes criem managers com arquivos temporários,
        # sem interferir nos dados reais do usuário.
        self.filepath = filepath

    def add(
        self,
        tipo: str,
        valor: float,
        categoria: str,
        descricao: str = "",
    ) -> dict:
        """Valida e registra uma nova transação.

        Raises:
            ValueError: se tipo inválido, valor não positivo ou categoria vazia.

        Returns:
            Dicionário com os dados da transação criada.
        """
        # Normaliza o tipo para minúsculas e remove espaços extras
        tipo = tipo.strip().lower()

        if tipo not in TIPOS_VALIDOS:
            raise ValueError(
                f"Tipo inválido: '{tipo}'. Use 'receita' ou 'despesa'."
            )
        if valor <= 0:
            raise ValueError(
                f"Valor deve ser positivo. Recebido: {valor}"
            )
        if not categoria.strip():
            raise ValueError("Categoria não pode ser vazia.")

        transaction = {
            "tipo": tipo,
            "valor": round(valor, 2),         # evita erros de ponto flutuante
            "categoria": categoria.strip().lower(),
            "descricao": descricao.strip(),
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        storage.add_transaction(transaction, self.filepath)
        return transaction

    def list_all(self) -> list[dict]:
        """Retorna todas as transações registradas."""
        return storage.load_transactions(self.filepath)

    def summary(self) -> dict:
        """Calcula receitas totais, despesas totais e saldo líquido."""
        transactions = self.list_all()
        receitas = sum(t["valor"] for t in transactions if t["tipo"] == "receita")
        despesas = sum(t["valor"] for t in transactions if t["tipo"] == "despesa")
        return {
            "receitas": round(receitas, 2),
            "despesas": round(despesas, 2),
            "saldo": round(receitas - despesas, 2),
        }

    def by_category(self) -> dict[str, float]:
        """Agrupa DESPESAS por categoria e retorna o total de cada uma.

        Receitas são ignoradas — interessa saber onde o dinheiro saiu.
        """
        totals: dict[str, float] = {}
        for t in self.list_all():
            if t["tipo"] == "despesa":
                cat = t["categoria"]
                totals[cat] = round(totals.get(cat, 0) + t["valor"], 2)
        return totals
