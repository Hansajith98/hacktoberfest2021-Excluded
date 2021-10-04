import requests
import json
import argparse
from re import sub
from bs4 import BeautifulSoup

urlList = {
    'thepiratebay': 'https://thepiratebay10.org/search/{query}/{page}/99/0',
    '1337x': 'https://1337x.to/search/{query}/{page}/'
}


def parse_args():
    parser = argparse.ArgumentParser(description='Meta-Search-Script for torrents.')
    parser.add_argument('query', metavar='QUERY', type=str,
                        help='the search term')
    parser.add_argument('-s', '--seeder-limit', dest='seeder_limit', type=int,
                        action='store', default=0,
                        help='minimum number of seeders')
    parser.add_argument('-c', '--categories', dest='categories', nargs='*', default=[],
                        help='the categories of the content')
    args = parser.parse_args()
    for i in range(len(args.categories)):
        args.categories[i] = args.categories[i].casefold()
    return args


def send_query(url):
    return requests.get(url)


def parse_thepiratebay(query, seeder_limit, categories):
    page = 1
    while (True):
        response = send_query(urlList['thepiratebay'].format_map({
            'query': query,
            'page': page})
        )
        if response.status_code != 200:
            break
        rawHtml = response.content
        soup = BeautifulSoup(rawHtml, 'html.parser')
        rows = soup.find('div', id='main-content').find_all('tr')[4:-1]
        if len(rows) == 0:
            break
        for row in rows:
            tds = row.find_all('td')
            if len(categories) > 0:
                if sub('\W+', ' ', tds[0].find('a').text).strip().casefold() not in categories:
                    continue
            if int(tds[2].text.strip()) < seeder_limit:
                continue
            yield {
                'category': sub('\W+', ' ', tds[0].find('a').text).strip(),
                'name': sub(
                    '[\n\t]+', ' ', tds[1].find('div', class_='detName').text
                ).strip(),
                'url': tds[1].find('a', href=True)['href'],
                'magnet-link': tds[1].find_all('a')[1]['href'],
                's': tds[2].text.strip(),
                'l': tds[3].text.strip()
            }
        page += 1


def parse_1337x():
    pass


def run(query, seeder_limit, categories):
    return [data for data in parse_thepiratebay(query, seeder_limit, categories)]


if __name__ == "__main__":
    args = parse_args()
    result = run(args.query, args.seeder_limit, args.categories)
    print(json.dumps(result, indent=4))
