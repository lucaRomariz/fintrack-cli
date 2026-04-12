# Como Contribuir

Obrigado por considerar contribuir com o FinTrack CLI!

## Fluxo de trabalho

1. Faça um **fork** do repositório
2. Crie uma branch a partir de `main`:
   ```bash
   git checkout -b feature/minha-funcionalidade
   ```
3. Implemente as alterações com commits descritivos
4. Garanta que os testes passam: `pytest tests/ -v`
5. Garanta que o lint está limpo: `ruff check src/ tests/`
6. Abra um **Pull Request** descrevendo o que foi feito e por quê

## Padrões de código

- Estilo verificado pelo `ruff` (PEP 8)
- Docstrings em português
- Testes devem cobrir caminho feliz, entradas inválidas e casos limite

## Ideias de contribuição

- Exportar relatório em PDF
- Filtro por data nas listagens
- Suporte a múltiplos perfis de usuário
- Interface gráfica com tkinter
