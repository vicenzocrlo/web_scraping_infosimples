from bs4 import BeautifulSoup
import requests
import json


def parse_price(price_str):
    """
    Converte uma string de preço no formato brasileiro (ex: 'R$ 4.799.990,00')
    para um valor float (4799990.0). Retorna None se não for possível converter.
    """
    if not price_str or not isinstance(price_str, str):
        return None
    try:
        clean_price = price_str.replace('R$', '').replace('.', '').replace(',', '.').strip()
        return float(clean_price)
    except (ValueError, TypeError):
        return None


url = 'https://infosimples.com/vagas/desafio/stellarcraft/product.html'

response = requests.get(url)
parsed_html = BeautifulSoup(response.content, 'html.parser')

resposta_final = {
    "title": parsed_html.select_one('h1#product_title').get_text(strip=True),
    "brand": parsed_html.select_one('.product-brand').get_text(strip=True)
}

resposta_final['categories'] = [link.get_text(strip=True) for link in parsed_html.select('.breadcrumb-bar nav a')]

description_meta = parsed_html.select_one('meta[itemprop="description"]')
resposta_final['description'] = description_meta.get('content', '') if description_meta else ""

resposta_final['skus'] = [
    {
        "name": sku.select_one('meta[itemprop="name"]').get('content', '') if sku.select_one('meta[itemprop="name"]') else "",
        "current_price": parse_price(sku.get('data-price')) if 'unavailable' not in sku.get('class', []) else None,
        "old_price": parse_price(sku.get('data-old-price')),
        "available": 'unavailable' not in sku.get('class', [])
    }
    for sku in parsed_html.select('.variant-btn')
]

resposta_final['specification'] = [
    {
        "label": cells[0].get_text(strip=True),
        "value": cells[1].get_text(strip=True)
    }
    for row in parsed_html.select('.specs-table tr')
    if (cells := row.select('td')) and len(cells) >= 2
]

def _extract_review(review):
    """Extrai dados de um elemento review."""
    score_stars = review.select_one('.review-stars')
    return {
        "name": review.select_one('.reviewer-name').get_text(strip=True) if review.select_one('.reviewer-name') else "",
        "date": review.select_one('.reviewer-date').get_text(strip=True) if review.select_one('.reviewer-date') else "",
        "score": score_stars.get_text(strip=True).count('★') if score_stars else 0,
        "text": review.select_one('.review-text').get_text(strip=True) if review.select_one('.review-text') else ""
    }

resposta_final['reviews'] = [_extract_review(review) for review in parsed_html.select('.review-card')]


if resposta_final['reviews']:
    avg = sum(r['score'] for r in resposta_final['reviews']) / len(resposta_final['reviews'])
    resposta_final['reviews_average_score'] = round(avg, 1)
else:
    resposta_final['reviews_average_score'] = 0.0

resposta_final['url'] = url

with open('produto.json', 'w', encoding='utf-8') as f:
    json.dump(resposta_final, f, ensure_ascii=False, indent=2)

print('Arquivo produto.json salvo com sucesso!')
