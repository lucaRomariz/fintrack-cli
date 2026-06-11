# 💰 FinTrack CLI

[![CI](https://github.com/lucaRomariz/fintrack-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/lucaRomariz/fintrack-cli/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Versão](https://img.shields.io/badge/versão-1.0.0-green.svg)](https://github.com/lucaRomariz/fintrack-cli/releases)
[![Licença: MIT](https://img.shields.io/badge/licença-MIT-yellow.svg)](./LICENSE)

> Gestor de gastos pessoais via linha de comando com geração automática de gráficos.

---

## 📋 Problema Real

O descontrole financeiro é uma das principais causas de endividamento no Brasil. Grande parte da população não utiliza nenhuma ferramenta de controle de gastos — seja pelo custo dos aplicativos, pela complexidade de uso ou pela falta de acesso a smartphones modernos.

O FinTrack CLI é uma solução **gratuita, acessível e sem necessidade de internet ou cadastro** para quem deseja começar a organizar as finanças pelo terminal.

---

## 💡 Proposta da Solução

Aplicação de linha de comando (CLI) que permite:

- Registrar receitas e despesas com categorias personalizadas
- Visualizar todas as transações registradas
- Consultar um resumo financeiro com saldo atual
- Gerar gráficos visuais de gastos, economia e evolução mensal

Os dados são armazenados localmente em `~/.fintrack/data.json`, sem dependência de serviços externos.

---

## Nova funcionalidade — Cotação em tempo real

O sistema agora possui integração com API pública utilizando a AwesomeAPI.

### 🎯 Objetivo
A partir de agora, o FinTrack CLI permite consultar a cotação do dólar (USD) em relação ao Real (BRL) em tempo real.

### 🔌 API Utilizada
- **AwesomeAPI**
- Endpoint: `https://economia.awesomeapi.com.br/last/USD-BRL`
- Método: `GET`

### 🛠️ Como funciona

Ao executar o comando:

```bash
fintrack cotacao
```

O sistema:

1. Envia uma requisição GET para a AwesomeAPI
2. Recebe os dados da cotação em formato JSON
3. Extrai o valor atual do dólar
4. Exibe a cotação formatada para o usuário

### 📝 Exemplo de uso

```bash
fintrack cotacao
```

### 📊 Exemplo de saída

```
╔══════════════════════════════╗
║    COTAÇÃO DO DÓLAR (USD/BRL)  ║
╠══════════════════════════════╣
║  Data da cotação: 2023-10-27   ║
║  Valor atual:     R$ 5,05      ║
╚══════════════════════════════╝
```

### 📁 Implementação

- Arquivo: [`cotacao_service.py`](fintrack/cotacao_service.py)
- Responsável por fazer a requisição HTTP e tratar a resposta

### 🧪 Testes

```bash
pytest tests/test_cotacao_service.py
```

## 👥 Público-Alvo

- Estudantes universitários que precisam controlar mesada e gastos mensais
- Jovens adultos iniciando vida financeira independente
- Microempreendedores individuais (MEIs) que precisam separar gastos pessoais dos do negócio
- Qualquer pessoa que queira controlar as finanças sem assinar um aplicativo pago

---

## ✨ Funcionalidades

| Comando | Descrição |
|---|---|
| `fintrack add` | Registrar receita ou despesa |
| `fintrack listar` | Listar transações (com filtro opcional) |
| `fintrack resumo` | Exibir total de receitas, despesas e saldo |
| `fintrack grafico` | Gerar gráfico: barras, pizza ou linha |
| `fintrack cotacao` | Exibir cotação do dólar |

**Tipos de gráfico disponíveis:**
- `resumo` — Barras comparando receitas × despesas com saldo destacado
- `categorias` — Pizza com distribuição de despesas por categoria
- `mensal` — Linha com evolução mês a mês

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11+ | Linguagem principal |
| matplotlib | ≥ 3.8 | Geração de gráficos |
| argparse | stdlib | Interface de linha de comando |
| pytest | ≥ 8.0 | Testes automatizados |
| ruff | ≥ 0.4 | Linting e análise estática |
| requests | ≥ 2.31 | Requisições HTTP para API de cotação |
| GitHub Actions | — | Integração contínua (CI) |

Armazenamento: **JSON local** em `~/.fintrack/data.json`

---

## 📦 Instalação

**Pré-requisitos:** Python 3.11+ e pip instalados.

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/fintrack-cli.git
cd fintrack-cli

# 2. Crie e ative um ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# ou
.venv\Scripts\activate          # Windows

# 3. Instale o projeto e suas dependências
pip install -e .
```

---

## ▶️ Como Usar

```bash
# Ver a versão instalada
fintrack --version

# Ver ajuda geral
fintrack --help

# Ver ajuda de um subcomando
fintrack add --help
```

### Exemplos práticos

```bash
# Registrar uma despesa
fintrack add --tipo despesa --valor 89.90 --categoria alimentacao --descricao "supermercado"

# Registrar uma receita
fintrack add --tipo receita --valor 3500.00 --categoria salario

# Listar todas as transações
fintrack listar

# Listar apenas despesas
fintrack listar --tipo despesa

# Ver resumo financeiro
fintrack resumo

# Gráfico de barras: receitas vs despesas (exibe na tela)
fintrack grafico --grafico resumo

# Gráfico de pizza: despesas por categoria
fintrack grafico --grafico categorias

# Gráfico de linha: evolução mensal
fintrack grafico --grafico mensal

# Salvar gráfico como PNG
fintrack grafico --grafico resumo --output grafico.png

# Exibir cotação do dólar
fintrack cotacao
```

### Exemplo de saída do `resumo`

```
╔══════════════════════════════╗
║     RESUMO FINANCEIRO        ║
╠══════════════════════════════╣
║  Receitas : R$      3.500,00 ║
║  Despesas : R$      1.245,90 ║
╠══════════════════════════════╣
║  Saldo    : R$      2.254,10 ║
║  ✅ Superávit                ║
╚══════════════════════════════╝
```

---

## 🧪 Como Rodar os Testes

```bash
# Instalar dependências de desenvolvimento
pip install -e ".[dev]"

# Rodar todos os testes com saída detalhada
pytest tests/ -v

# Com relatório de cobertura
pytest tests/ -v --cov=src/fintrack
```

Resultado esperado: **19 testes passando**.

---

## 🔍 Como Rodar o Lint

```bash
# Verificar problemas no código
ruff check src/ tests/

# Aplicar correções automáticas seguras
ruff check src/ tests/ --fix
```

---

## 🔄 Pipeline de CI

A cada `push` ou `pull request` para `main`, o GitHub Actions executa automaticamente:

1. Checkout do código
2. Configuração do Python (3.11 e 3.12)
3. Instalação das dependências
4. **Ruff** — análise estática
5. **Pytest** — testes automatizados

Configuração: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

---

## 📁 Estrutura do Projeto

```
fintrack-cli/
├── src/
│   └── fintrack/
│       ├── __init__.py      # Versão do pacote (1.0.0)
│       ├── main.py          # Interface CLI (argparse)
│       ├── manager.py       # Regras de negócio
│       ├── storage.py       # Persistência em JSON
│       ├── charts.py        # Gráficos com matplotlib
│       └── cotacao_service.py # Serviço de cotação do dólar
├── tests/
│   ├── test_manager.py      # 15 testes de lógica
│   └── test_storage.py      # 5 testes de persistência
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline de CI
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
└── pyproject.toml           # Manifesto: versão, deps, config
```

---

## 📌 Versão Atual

**1.0.0** — Consulte o [CHANGELOG](./CHANGELOG.md) para o histórico completo.

---

## 👤 Autor

**Luca Romariz**
- GitHub: [@lucaRomariz](https://github.com/SEU_USUARIO)
- Repositório: [github.com/lucaRomariz/fintrack-cli](https://github.com/lucaRomariz/fintrack-cli)

---

## 📄 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](./LICENSE) para detalhes.
