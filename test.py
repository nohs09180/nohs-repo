path = 'input.txt'

fizz_dict = {}
result_list = []

with open(path) as f:
    for s_line in f:
        s_line = s_line.split(':')
        if len(s_line) > 1:
            fizz_dict[int(s_line[0])] = s_line[1][:-1]
        else:
            num = int(s_line[0][:-1])

num_list = list(fizz_dict.keys())
num_list = sorted(num_list)

for i in num_list:
    if num % i == 0:
        result_list.append(fizz_dict[i])
result = ''.join(result_list)

if len(result_list) == 0:
    result = num

print(result)