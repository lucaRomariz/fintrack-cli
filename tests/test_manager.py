"""Testes do FinancialManager — lógica de negócio.

Cada teste usa tmp_path (fixture nativa do pytest) para criar
um arquivo JSON temporário e isolado. Assim os testes nunca
interferem nos dados reais do usuário nem entre si.
"""

import pytest

from fintrack.manager import FinancialManager


# ── Fixture: cria um manager com arquivo temporário ──────────
@pytest.fixture
def manager(tmp_path):
    """Manager isolado para cada teste."""
    return FinancialManager(filepath=tmp_path / "test.json")


# ── Caminho feliz: adições válidas ───────────────────────────

def test_add_despesa_retorna_dict_correto(manager):
    """Uma despesa válida deve retornar dicionário com todos os campos."""
    t = manager.add(
        tipo="despesa", valor=150.0, categoria="alimentacao", descricao="mercado"
    )
    assert t["tipo"] == "despesa"
    assert t["valor"] == 150.0
    assert t["categoria"] == "alimentacao"
    assert t["descricao"] == "mercado"
    assert "data" in t


def test_add_receita_retorna_dict_correto(manager):
    """Uma receita válida deve ser registrada corretamente."""
    t = manager.add(tipo="receita", valor=3000.0, categoria="salario")
    assert t["tipo"] == "receita"
    assert t["valor"] == 3000.0


def test_add_persiste_na_listagem(manager):
    """Transação adicionada deve aparecer em list_all()."""
    manager.add(tipo="despesa", valor=50.0, categoria="transporte")
    assert len(manager.list_all()) == 1


def test_add_multiplas_acumulam(manager):
    """Múltiplas adições devem acumular na lista."""
    manager.add(tipo="receita", valor=2000.0, categoria="salario")
    manager.add(tipo="despesa", valor=300.0, categoria="alimentacao")
    manager.add(tipo="despesa", valor=100.0, categoria="transporte")
    assert len(manager.list_all()) == 3


def test_tipo_aceito_em_maiusculas(manager):
    """O tipo deve ser normalizado para minúsculas automaticamente."""
    t = manager.add(tipo="DESPESA", valor=10.0, categoria="teste")
    assert t["tipo"] == "despesa"


def test_add_valor_centavos(manager):
    """Deve aceitar valores pequenos como R$ 0,01."""
    t = manager.add(tipo="despesa", valor=0.01, categoria="outros")
    assert t["valor"] == 0.01


# ── Entradas inválidas: devem lançar ValueError ───────────────

def test_tipo_invalido_levanta_erro(manager):
    with pytest.raises(ValueError, match="Tipo inválido"):
        manager.add(tipo="investimento", valor=100.0, categoria="acoes")


def test_valor_zero_levanta_erro(manager):
    with pytest.raises(ValueError, match="Valor deve ser positivo"):
        manager.add(tipo="despesa", valor=0.0, categoria="teste")


def test_valor_negativo_levanta_erro(manager):
    with pytest.raises(ValueError, match="Valor deve ser positivo"):
        manager.add(tipo="despesa", valor=-50.0, categoria="teste")


def test_categoria_vazia_levanta_erro(manager):
    with pytest.raises(ValueError, match="Categoria não pode ser vazia"):
        manager.add(tipo="despesa", valor=10.0, categoria="   ")


# ── Summary ──────────────────────────────────────────────────

def test_summary_saldo_positivo(manager):
    manager.add(tipo="receita", valor=1000.0, categoria="salario")
    manager.add(tipo="despesa", valor=400.0, categoria="aluguel")
    s = manager.summary()
    assert s["receitas"] == 1000.0
    assert s["despesas"] == 400.0
    assert s["saldo"] == 600.0


def test_summary_saldo_negativo(manager):
    manager.add(tipo="receita", valor=500.0, categoria="freelance")
    manager.add(tipo="despesa", valor=800.0, categoria="aluguel")
    assert manager.summary()["saldo"] == -300.0


def test_summary_base_vazia(manager):
    assert manager.summary() == {"receitas": 0.0, "despesas": 0.0, "saldo": 0.0}


# ── By category ──────────────────────────────────────────────

def test_by_category_soma_mesma_categoria(manager):
    manager.add(tipo="despesa", valor=100.0, categoria="alimentacao")
    manager.add(tipo="despesa", valor=50.0, categoria="alimentacao")
    manager.add(tipo="despesa", valor=200.0, categoria="aluguel")
    by_cat = manager.by_category()
    assert by_cat["alimentacao"] == 150.0
    assert by_cat["aluguel"] == 200.0


def test_by_category_ignora_receitas(manager):
    manager.add(tipo="receita", valor=3000.0, categoria="salario")
    manager.add(tipo="despesa", valor=100.0, categoria="alimentacao")
    by_cat = manager.by_category()
    assert "salario" not in by_cat


def test_by_category_sem_despesas_retorna_vazio(manager):
    manager.add(tipo="receita", valor=1000.0, categoria="salario")
    assert manager.by_category() == {}
