players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
new_list = []
for key, value in players.items():
    new_list.append(key + value)
print(new_list)
