import requests
import json


def main():
    all_deaths_response = requests.get('https://www.breakingbadapi.com/api/deaths/')
    all_deaths = json.loads(all_deaths_response.text)

    # max_episode_all = {}
    # max_deaths = 0

    #  предлагаю упростить выборку словаря с максимальным количеством смертей.
    #  Стоит передать список словарей deaths в функцию max, если в параметр key функции передать lambda функцию,
    #  То, сможет найти словарь с максимальным значением по интересующему нас ключу в одну строку кода.

    # for episode in all_deaths:
    #     if episode['number_of_deaths'] > max_deaths:
    #         max_deaths = episode['number_of_deaths']
    #         max_episode_all = episode

    max_episode_all = max(all_deaths, key=lambda x: x['number_of_deaths'])

    max_deaths_episode = {
        'death_id': max_episode_all['death_id'],
        'season': max_episode_all['season'],
        'episode': max_episode_all['episode'],
        'number_of_deaths': max_episode_all['number_of_deaths'],
        'death': max_episode_all['death']
    }

    print(max_deaths_episode)
    with open('max_deaths_file.json', 'w') as file:
        json.dump(max_deaths_episode, file, indent=4)


if __name__ == '__main__':
    main()
