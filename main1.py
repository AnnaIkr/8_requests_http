import requests

#url = 'https://akabab.github.io/superhero-api/api'

urls = [
    f'https://akabab.github.io/superhero-api/api/search/Hulk',
    f'https://akabab.github.io/superhero-api/api/search/Captain%America',
    f'https://akabab.github.io/superhero-api/api/search/Thanos'
]

def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r


def parser():
    heroes_list = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                heroes_list .append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print('Ошибка')

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in heroes_list:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")


parser()