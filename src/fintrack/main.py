"""Interface de linha de comando do FinTrack.

Estrutura com subcomandos (igual ao git):
  fintrack add      → registra transação
  fintrack listar   → lista transações
  fintrack resumo   → exibe saldo
  fintrack grafico  → gera gráfico
"""

import argparse
import sys
from pathlib import Path
from fintrack.cotacao_service import obter_cotacao_dolar

from fintrack import __version__
from fintrack.charts import plot_by_category, plot_monthly_evolution, plot_summary
from fintrack.manager import FinancialManager
from fintrack.sync_service import sync_transactions

# ──────────────────────────────────────────────────────────────
# Handlers: uma função por subcomando
# Cada handler recebe os args parseados e o manager já instanciado.
# Retorna 0 (sucesso) ou 1 (erro) — convenção Unix.
# ──────────────────────────────────────────────────────────────

def cmd_add(args: argparse.Namespace, manager: FinancialManager) -> int:
    """Registra uma nova transação e confirma para o usuário."""
    try:
        t = manager.add(
            tipo=args.tipo,
            valor=args.valor,
            categoria=args.categoria,
            descricao=args.descricao or "",
        )
        emoji = "💰" if t["tipo"] == "receita" else "💸"
        print(
            f"\n{emoji}  Transação registrada!\n"
            f"   Tipo     : {t['tipo'].capitalize()}\n"
            f"   Valor    : R$ {t['valor']:,.2f}\n"
            f"   Categoria: {t['categoria']}\n"
            f"   Data     : {t['data']}\n"
        )
        return 0
    except ValueError as exc:
        # ValueError vem das validações do manager — mensagem já é clara
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


def cmd_list(args: argparse.Namespace, manager: FinancialManager) -> int:
    """Lista transações com filtro opcional por tipo."""
    transactions = manager.list_all()

    if not transactions:
        print("Nenhuma transação registrada ainda.")
        return 0

    tipo_filter = args.tipo.lower() if args.tipo else None
    filtered = [
        t for t in transactions
        if tipo_filter is None or t["tipo"] == tipo_filter
    ]

    if not filtered:
        print(f"Nenhuma transação do tipo '{tipo_filter}' encontrada.")
        return 0

    # Cabeçalho da tabela
    print(
        f"\n{'#':<4} {'Tipo':<10} {'Valor':>12}"
        f"  {'Categoria':<16} {'Data':<20}  Descrição"
    )
    print("─" * 75)
    for i, t in enumerate(filtered, 1):
        print(
            f"{i:<4} {t['tipo'].capitalize():<10} R$ {t['valor']:>9,.2f}  "
            f"{t['categoria']:<16} {t['data']:<20}  {t['descricao']}"
        )
    print(f"\n{len(filtered)} transação(ões) encontrada(s).\n")
    return 0


def cmd_summary(_args: argparse.Namespace, manager: FinancialManager) -> int:
    """Exibe resumo com receitas, despesas e saldo."""
    s = manager.summary()
    status = "✅ Superávit" if s["saldo"] >= 0 else "⚠️  Déficit"
    print(
        "\n╔══════════════════════════════╗\n"
        "║     RESUMO FINANCEIRO        ║\n"
        "╠══════════════════════════════╣\n"
        f"║  Receitas : R$ {s['receitas']:>12,.2f}  ║\n"
        f"║  Despesas : R$ {s['despesas']:>12,.2f}  ║\n"
        "╠══════════════════════════════╣\n"
        f"║  Saldo    : R$ {s['saldo']:>12,.2f}  ║\n"
        f"║  {status:<28}║\n"
        "╚══════════════════════════════╝\n"
    )
    return 0


def cmd_chart(args: argparse.Namespace, manager: FinancialManager) -> int:
    """Gera o gráfico escolhido."""
    output = Path(args.output) if args.output else None
    tipo = args.grafico.lower()

    if tipo == "resumo":
        s = manager.summary()
        plot_summary(s["receitas"], s["despesas"], output)
    elif tipo == "categorias":
        plot_by_category(manager.by_category(), output)
    elif tipo == "mensal":
        plot_monthly_evolution(manager.list_all(), output)
    else:
        print(f"Gráfico desconhecido: '{tipo}'", file=sys.stderr)
        return 1
    return 0

def cmd_cotacao(_args: argparse.Namespace, _manager: FinancialManager) -> int:
    """Exibe a cotação atual do dólar."""

    cotacao = obter_cotacao_dolar()

    if cotacao:
        print(
            "\n💵 COTAÇÃO DO DÓLAR\n"
            "═══════════════════════\n"
            f"USD → BRL = R$ {cotacao:.2f}\n"
        )
        return 0

    print("Não foi possível obter a cotação.")
    return 1

def cmd_sync(_args, _manager):

    total = sync_transactions()

    print(
        "\n☁️ SINCRONIZAÇÃO CONCLUÍDA\n"
        "════════════════════════════\n"
        f"{total} transações enviadas para o Supabase.\n"
    )

    return 0

# ──────────────────────────────────────────────────────────────
# Construção do parser de argumentos
# ──────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """Monta e retorna o parser completo com todos os subcomandos."""
    parser = argparse.ArgumentParser(
        prog="fintrack",
        description="💰 FinTrack CLI — Gestor de gastos pessoais",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    sub = parser.add_subparsers(dest="comando", metavar="<comando>")
    sub.required = True

    # ── add ──────────────────────────────────────────────────
    p_add = sub.add_parser("add", help="Registrar uma nova transação")
    p_add.add_argument(
        "--tipo", required=True, choices=["receita", "despesa"],
        help="Tipo da transação"
    )
    p_add.add_argument("--valor", required=True, type=float, help="Valor em reais")
    p_add.add_argument("--categoria", required=True, help="Categoria da transação")
    p_add.add_argument("--descricao", default="", help="Descrição opcional")

    # ── listar ───────────────────────────────────────────────
    p_list = sub.add_parser("listar", help="Listar transações registradas")
    p_list.add_argument(
        "--tipo", choices=["receita", "despesa"], default=None,
        help="Filtrar por tipo"
    )

    # ── resumo ───────────────────────────────────────────────
    sub.add_parser("resumo", help="Exibir resumo financeiro")

    # ── grafico ──────────────────────────────────────────────
    p_chart = sub.add_parser("grafico", help="Gerar gráfico financeiro")
    p_chart.add_argument(
        "--grafico",
        choices=["resumo", "categorias", "mensal"],
        default="resumo",
        help="Tipo de gráfico (padrão: resumo)",
    )
    p_chart.add_argument(
        "--output", default=None,
        help="Salvar gráfico em arquivo PNG (ex: grafico.png)"
    )

    # ── cotacao ──────────────────────────────────────────────
    sub.add_parser("cotacao", help="Exibir cotação atual do dólar")

    # ── sync ─────────────────────────────────────────────────
    sub.add_parser(
        "sync",
        help="Sincronizar dados com o banco Supabase"
    )
    
    return parser


# ──────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────

def main() -> None:
    """Ponto de entrada registrado no pyproject.toml."""
    parser = build_parser()
    args = parser.parse_args()
    manager = FinancialManager()

    handlers = {
        "add": cmd_add,
        "listar": cmd_list,
        "resumo": cmd_summary,
        "grafico": cmd_chart,
        "cotacao": cmd_cotacao,
        "sync": cmd_sync
    }

    sys.exit(handlers[args.comando](args, manager))


if __name__ == "__main__":
    main()
