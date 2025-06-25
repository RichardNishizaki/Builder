# Projeto Builder

Este projeto é uma implementação prática do **Padrão de Projeto Builder** usando Python.

## 💡 Objetivo

Demonstrar como o padrão Builder pode ser utilizado para construir objetos complexos de forma controlada e passo a passo — neste caso, o exemplo gira em torno da construção de uma **Nota Fiscal**.

## 📁 Estrutura

- `main.py`: ponto de entrada do sistema
- `NotaFiscalBuilder.py`: responsável por montar a nota fiscal
- `NotaFiscal.py`: classe final da nota construída
- `AcaoAposGerarNota.py`: interface para ações pós-construção
- `EnviadorDeEmail.py`, `NotaFiscalDao.py`, `Impressora.py`: ações executadas após criação

## 🔧 Tecnologias

- Python 3.x
- Padrões de Projeto: Builder + Observer

## ▶️ Como Executar

Certifique-se de ter o Python instalado e execute:

```bash
python main.py
