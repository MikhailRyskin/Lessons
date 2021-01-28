import random

team_1 = [round((random.random() * (10 - 5) + 5), 2) for _ in range(20)]
team_2 = [round((random.random() * (10 - 5) + 5), 2) for _ in range(20)]
winner_list = [(team_1[ind] if team_1[ind] > team_2[ind] else team_2[ind]) for ind in range(20)]
print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winner_list)

# зачёт!
