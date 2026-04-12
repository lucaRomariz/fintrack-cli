"""Camada de persistência: lê e grava transações em arquivo JSON."""

import json
from pathlib import Path

# Arquivo padrão fica em ~/.fintrack/data.json
# Path.home() retorna a pasta home do usuário em qualquer sistema operacional
DEFAULT_DATA_FILE = Path.home() / ".fintrack" / "data.json"


def _ensure_dir(path: Path) -> None:
    """Cria o diretório pai do arquivo caso ele não exista ainda."""
    path.parent.mkdir(parents=True, exist_ok=True)


def load_transactions(filepath: Path = DEFAULT_DATA_FILE) -> list[dict]:
    """Lê o arquivo JSON e retorna a lista de transações.

    Se o arquivo ainda não existir (primeira execução), retorna lista vazia
    em vez de lançar erro — comportamento seguro e esperado.
    """
    if not filepath.exists():
        return []
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def save_transactions(
    transactions: list[dict], filepath: Path = DEFAULT_DATA_FILE
) -> None:
    """Sobrescreve o arquivo JSON com a lista completa de transações.

    ensure_ascii=False preserva acentos.
    indent=2 deixa o JSON legível caso o usuário queira abrir o arquivo.
    """
    _ensure_dir(filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(transactions, f, ensure_ascii=False, indent=2)


def add_transaction(
    transaction: dict, filepath: Path = DEFAULT_DATA_FILE
) -> None:
    """Carrega a lista atual, adiciona uma transação e salva de volta."""
    transactions = load_transactions(filepath)
    transactions.append(transaction)
    save_transactions(transactions, filepath)


def clear_transactions(filepath: Path = DEFAULT_DATA_FILE) -> None:
    """Apaga todas as transações. Usado nos testes para isolar cada caso."""
    save_transactions([], filepath)
