"""Testes da camada de persistência (storage.py).

Verifica que o JSON é lido, salvo e modificado corretamente.
"""

import json

import pytest

from fintrack import storage


@pytest.fixture
def temp_file(tmp_path):
    """Arquivo JSON temporário e isolado para cada teste."""
    return tmp_path / "test_storage.json"


def test_load_arquivo_inexistente_retorna_lista_vazia(temp_file):
    """Primeira execução: arquivo não existe → deve retornar [] sem erro."""
    result = storage.load_transactions(temp_file)
    assert result == []


def test_save_e_load_preservam_dados(temp_file):
    """Salvar e carregar deve retornar exatamente os mesmos dados."""
    data = [{"tipo": "despesa", "valor": 99.9, "categoria": "teste"}]
    storage.save_transactions(data, temp_file)
    assert storage.load_transactions(temp_file) == data


def test_add_transaction_incrementa_lista(temp_file):
    """Cada add_transaction deve aumentar a lista em exatamente 1 item."""
    storage.add_transaction({"tipo": "receita", "valor": 500.0}, temp_file)
    storage.add_transaction({"tipo": "despesa", "valor": 100.0}, temp_file)
    assert len(storage.load_transactions(temp_file)) == 2


def test_clear_transactions_esvazia_arquivo(temp_file):
    """clear_transactions deve deixar a lista vazia."""
    storage.add_transaction({"tipo": "receita", "valor": 10.0}, temp_file)
    storage.clear_transactions(temp_file)
    assert storage.load_transactions(temp_file) == []


def test_arquivo_gerado_e_json_valido(temp_file):
    """O arquivo salvo deve ser um JSON válido e legível."""
    data = [{"tipo": "despesa", "valor": 42.0, "categoria": "alimentacao"}]
    storage.save_transactions(data, temp_file)
    with open(temp_file) as f:
        parsed = json.load(f)
    assert parsed == data
