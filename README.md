# 💰 FinTrack CLI

[![CI](https://github.com/lucaRomariz/fintrack-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/lucaRomariz/fintrack-cli/actions/workflows/ci.yml)

Sistema de gestão financeira pessoal via linha de comando desenvolvido em Python, com persistência local em JSON, consulta de cotação em tempo real, geração de gráficos e sincronização com banco de dados PostgreSQL hospedado no Supabase.

---

# 📋 Problema

Muitas pessoas não possuem uma forma simples e gratuita de acompanhar receitas, despesas e evolução financeira.

O FinTrack CLI foi desenvolvido para oferecer uma solução leve e acessível diretamente pelo terminal.

---

# 🎯 Objetivo

Permitir que o usuário:

* Registre receitas e despesas
* Consulte saldo financeiro
* Gere gráficos financeiros
* Consulte a cotação do dólar em tempo real
* Sincronize seus dados para um banco de dados em nuvem

---

# ✨ Funcionalidades

| Comando          | Descrição                      |
| ---------------- | ------------------------------ |
| fintrack add     | Registrar receita ou despesa   |
| fintrack listar  | Listar transações              |
| fintrack resumo  | Exibir resumo financeiro       |
| fintrack grafico | Gerar gráficos                 |
| fintrack cotacao | Consultar cotação do dólar     |
| fintrack sync    | Sincronizar dados com Supabase |

---

# ☁️ Integração com Banco de Dados

O projeto utiliza PostgreSQL hospedado no Supabase para persistência dos dados em nuvem.

## Tecnologias

* Supabase
* PostgreSQL
* psycopg2-binary
* python-dotenv

## Fluxo

Usuário

↓

CLI (main.py)

↓

FinancialManager

↓

storage.py (JSON)

↓

sync_service.py

↓

db_storage.py

↓

database.py

↓

Supabase PostgreSQL

---

# 🌎 Integração com API Externa

O sistema utiliza a AwesomeAPI para consulta da cotação do dólar em tempo real.

### Comando

```bash
fintrack cotacao
```

### Exemplo

```text
💵 COTAÇÃO DO DÓLAR

USD → BRL = R$ 5.42
```

---

# 📊 Geração de Gráficos

Tipos disponíveis:

* Resumo Financeiro
* Gastos por Categoria
* Evolução Mensal

Exemplo:

```bash
fintrack grafico --grafico categorias
```

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia      | Finalidade          |
| --------------- | ------------------- |
| Python 3.11+    | Linguagem principal |
| PostgreSQL      | Banco de Dados      |
| Supabase        | Banco em nuvem      |
| psycopg2-binary | Conexão PostgreSQL  |
| Requests        | Consumo de API      |
| Matplotlib      | Gráficos            |
| Pytest          | Testes              |
| Ruff            | Lint                |
| GitHub Actions  | CI/CD               |

---

# 🧪 Testes

Executar:

```bash
pytest -v
```

O projeto possui testes automatizados para:

* Regras de negócio
* Persistência
* Integração da API
* Sincronização

---

# 🔄 Integração Contínua

A pipeline do GitHub Actions executa automaticamente:

1. Instalação das dependências
2. Ruff
3. Pytest
4. Validação para Pull Requests

Nenhum código é integrado à branch principal sem aprovação da pipeline.

---

# 🤝 Trabalho Colaborativo

O projeto foi desenvolvido utilizando:

* GitHub Projects
* Issues
* Branches
* Pull Requests
* Code Review
* GitHub Actions

Cada integrante realizou contribuições por meio de Pull Requests revisados e aprovados por outro membro da equipe.

---

# 👥 Integrantes

| Nome         |
| ------------ |
| Luca Romariz |
| Miguel       |

---

# 📁 Estrutura do Projeto

```text
fintrack-cli/

src/fintrack/

main.py

manager.py

storage.py

database.py

db_storage.py

sync_service.py

cotacao_service.py

charts.py

tests/

.github/workflows/

README.md
```

---

# 🚀 Como Executar

```bash
git clone https://github.com/lucaRomariz/fintrack-cli.git

cd fintrack-cli

python -m venv .venv

source .venv/bin/activate

pip install -e .
```

---

# 📌 Repositório

https://github.com/lucaRomariz/fintrack-cli

---

# 📄 Licença

MIT License.
