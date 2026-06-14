# Arquitetura do FinTrack CLI

## Visão Geral

O FinTrack CLI é uma aplicação de linha de comando desenvolvida em Python para gerenciamento financeiro pessoal.
A aplicação permite registrar receitas e despesas, gerar gráficos, consultar a cotação do dólar 
e sincronizar dados para um banco PostgreSQL hospedado no Supabase.

## Arquitetura Geral

Usuário
↓
CLI (main.py)
↓
FinancialManager
↓
Storage JSON
Fluxo de sincronização:
Storage JSON
↓
sync_service.py
↓
db_storage.py
↓
database.py
↓
Supabase PostgreSQL

## Responsabilidades

### main.py

Interface de linha de comando.
### manager.py
Regras de negócio.
### storage.py
Persistência local em JSON.
### db_storage.py
Operações de banco de dados