import json
import re

import requests
from bs4 import BeautifulSoup

from flask import Flask, request, jsonify

app = Flask(__name__)


def parse_medium_article(html):
    soup = BeautifulSoup(html, 'html.parser')

    script = soup.select_one('script[type="application/ld+json"]')
    if not script:
        return

    json_data = script.text
    data = json.loads(json_data)

    article = {}
    article['title'] = data.get('name')
    article['id'] = data.get('articleId')
    article['published_date'] = data.get('datePublished')
    article['modified_date'] = data.get('dateModified')
    article['reading_time'] = soup.select_one('span.readingTime')['title']
    article['thumbnail'] = data.get('thumbnailUrl')
    article['url'] = data.get('url')
    article['author'] = data.get('author', {}).get('name')
    article['author_url'] = data.get('author', {}).get('url')
    article['publisher'] = data.get('publisher', {}).get('name')
    article['publisher_url'] = data.get('publisher', {}).get('url')
    article['keywords'] = [keyword.replace('Tag:', '') for keyword in data.get('keywords', []) if
                           keyword.startswith('Tag:')]
    article['claps'] = re.findall('totalClapCount":(\d+)', html)[0]
    article['subtitle'] = re.findall('subtitle":"(.*?)",', html)[0]
    # article['article'] = str(soup.select_one('div.sectionLayout--insetColumn'))
    return article


# example url: 127.0.0.1:5000/medium?url=https://medium.com/@sagunshrestha/analyzing-cnets-headlines-3f350bb97cd4
@app.route('/medium')
def medium():
    url = request.args.get('url', '')
    try:
        response = requests.get(url)
    except Exception as e:
        return jsonify({'Status': 'Exception', 'Message': str(e)})

    if response.ok:
        article = parse_medium_article(response.text)
    else:
        article = {'Status': response.status_code, 'Message Type': 'Error'}
    return jsonify(article)


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run()
