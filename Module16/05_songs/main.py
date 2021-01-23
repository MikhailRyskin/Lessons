violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
number_songs = int(input('Сколько песен выбрать? '))
total_duration = 0
for num in range(number_songs):
    print('Название', num + 1, 'песни:', end=' ')
    song = input('')
    for ind in range(len(violator_songs)):
        if violator_songs[ind][0] == song:
            total_duration += violator_songs[ind][1]
print('Общее время звучания песен:', round(total_duration, 2), 'минут')

# зачёт!
