# Web Scraper - Infosimples Challenge

Web scraper em Python que coleta dados do produto Corellian YT-1300f Light Freighter.

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Execute o script principal:
```bash
python scraper.py
```

O arquivo `produto.json` será gerado com todos os dados extraídos.

## Estrutura

- `scraper.py`: Script principal que realiza o web scraping
- `requirements.txt`: Dependências do projeto
- `produto.json`: Arquivo JSON gerado com os dados extraídos
- `.gitgnore`: Arquivo para definir quais arquivos ignorar

## Dados Extraídos

O arquivo `produto.json` contém todos os tópicos cobrados na tabela abaixo, respeitando seus respectivos tipos e segmentos:

<img width="644" height="698" alt="image" src="https://github.com/user-attachments/assets/0705a478-ea5b-454f-a792-62c2b213b180" />

## Tecnologias Utilizadas

- **BeautifulSoup**: Para parsing do HTML
- **Requests**: Para requisições HTTP
- **Python 3.13+**
- **Claude Haiku 4.5**: Para auxiliar na construção do projeto
- **Gemini 3.5 Flash**: Para dúvidas simples e revisão
