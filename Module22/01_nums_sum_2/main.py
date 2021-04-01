file = open('numbers.txt', 'r')
numbers = file.read().split()
file.close()

summ = 0
for number in numbers:
    summ += int(number)

out_file = open('answer.txt', 'w')
out_file.write(str(summ))
out_file.close()
