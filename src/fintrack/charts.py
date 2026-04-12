"""Geração de gráficos financeiros com matplotlib.

Cada função aceita output_path opcional:
- None  → exibe na tela (plt.show)
- Path  → salva como imagem (plt.savefig)

Isso torna as funções flexíveis: funcionam no terminal e em testes.
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def plot_summary(
    receitas: float, despesas: float, output_path: Path | None = None
) -> None:
    """Gráfico de barras: receitas × despesas com saldo destacado."""
    labels = ["Receitas", "Despesas"]
    values = [receitas, despesas]
    colors = ["#2ecc71", "#e74c3c"]   # verde para receita, vermelho para despesa

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(labels, values, color=colors, width=0.45, edgecolor="white")

    # Rótulo com valor em cima de cada barra
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(values) * 0.02,
            f"R$ {val:,.2f}",
            ha="center",
            fontsize=12,
            fontweight="bold",
        )

    saldo = receitas - despesas
    saldo_color = "#2ecc71" if saldo >= 0 else "#e74c3c"
    patch = mpatches.Patch(color=saldo_color, label=f"Saldo: R$ {saldo:,.2f}")
    ax.legend(handles=[patch], fontsize=11)

    ax.set_title("Resumo Financeiro", fontsize=15, fontweight="bold", pad=15)
    ax.set_ylabel("Valor (R$)", fontsize=11)
    ax.set_facecolor("#f9f9f9")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"R$ {x:,.0f}")
    )

    plt.tight_layout()
    _output(output_path)


def plot_by_category(
    by_category: dict[str, float], output_path: Path | None = None
) -> None:
    """Gráfico de pizza: distribuição das despesas por categoria."""
    if not by_category:
        print("Nenhuma despesa registrada para gerar este gráfico.")
        return

    labels = list(by_category.keys())
    values = list(by_category.values())

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",          # mostra porcentagem em cada fatia
        startangle=140,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )
    ax.set_title("Despesas por Categoria", fontsize=15, fontweight="bold", pad=15)
    plt.tight_layout()
    _output(output_path)


def plot_monthly_evolution(
    transactions: list[dict], output_path: Path | None = None
) -> None:
    """Gráfico de linha: evolução mensal de receitas e despesas."""
    from collections import defaultdict

    # Agrupa por "YYYY-MM" para ordenar cronologicamente
    monthly: dict[str, dict[str, float]] = defaultdict(
        lambda: {"receita": 0.0, "despesa": 0.0}
    )
    for t in transactions:
        mes = t["data"][:7]          # "2025-01-15 14:00:00" → "2025-01"
        monthly[mes][t["tipo"]] += t["valor"]

    if not monthly:
        print("Nenhuma transação para gerar este gráfico.")
        return

    meses = sorted(monthly.keys())
    receitas = [monthly[m]["receita"] for m in meses]
    despesas = [monthly[m]["despesa"] for m in meses]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(
        meses, receitas, marker="o", color="#2ecc71", linewidth=2.5, label="Receitas"
    )
    ax.plot(
        meses, despesas, marker="s", color="#e74c3c", linewidth=2.5, label="Despesas"
    )
    ax.fill_between(meses, receitas, despesas, alpha=0.1, color="#3498db")

    ax.set_title("Evolução Mensal", fontsize=15, fontweight="bold", pad=15)
    ax.set_xlabel("Mês")
    ax.set_ylabel("Valor (R$)")
    ax.legend(fontsize=11)
    ax.set_facecolor("#f9f9f9")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"R$ {x:,.0f}")
    )
    plt.xticks(rotation=30)
    plt.tight_layout()
    _output(output_path)


def _output(output_path: Path | None) -> None:
    """Exibe ou salva o gráfico e libera a memória."""
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        print(f"Gráfico salvo em: {output_path}")
    else:
        plt.show()
    plt.close()   # sempre libera a figura da memória
