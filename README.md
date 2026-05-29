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

## Dados Extraídos

O arquivo `produto.json` contém:
- **title**: Título do produto
- **brand**: Marca do produto
- **categories**: Categorias do produto
- **description**: Descrição completa
- **skus**: Variações do produto com preços e disponibilidade
- **specification**: Especificações técnicas
- **reviews**: Avaliações dos clientes
- **reviews_average_score**: Nota média das avaliações
- **url**: URL da página

## Tecnologias Utilizadas

- **BeautifulSoup**: Para parsing do HTML
- **Requests**: Para requisições HTTP
- **Python 3.13+**
