# Changelog

Todas as mudanças notáveis deste projeto estão documentadas aqui.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).
Este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [1.0.0] — 2026-04-12

### Adicionado
- Registro de transações financeiras (receitas e despesas) via CLI
- Listagem de transações com filtro por tipo
- Resumo financeiro com cálculo de saldo líquido
- Gráfico de barras: receitas × despesas
- Gráfico de pizza: despesas por categoria
- Gráfico de linha: evolução mensal
- Persistência local em JSON (`~/.fintrack/data.json`)
- 19 testes automatizados com pytest
- Análise estática com ruff
- Pipeline de CI com GitHub Actions (Python 3.11 e 3.12)
