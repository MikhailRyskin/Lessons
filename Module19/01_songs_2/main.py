violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
numb_songs = int(input('Сколько песен выбрать? '))
total_time = 0
for ind in range(1, numb_songs + 1):
    song_title = input(f'Название {ind} песни: ')
    total_time += violator_songs.get(song_title, 0)
print(f'Общее время звучания песен: {round(total_time, 2)} минут')

# зачёт!
