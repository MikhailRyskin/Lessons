file = open('zen.txt', 'r')
text_list = []
for line in file:
    text_list.append(line)
file.close()

for line in text_list[::-1]:
    print(line, end='')

# зачёт!
