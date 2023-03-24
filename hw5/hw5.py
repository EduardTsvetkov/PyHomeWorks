# s = '-8-5+234-18'
# result = 0
# prev_op = '+'
# prev_op_ind = -1
# for i in range(0, len(s)):
#     if s[i] == '+' or s[i] == '-':
#         if i == 0:  # если первое число отрицательное
#             prev_op = s[i]
#             prev_op_ind = i
#             continue

#         n = int(s[prev_op_ind + 1: i])

#         if prev_op == '+':
#             result += n
#         elif prev_op == '-':
#             result -= n
#         prev_op = s[i]
#         prev_op_ind = i

# if prev_op == '+':  # обрабатываем последнее число
#     result += int(s[prev_op_ind + 1: len(s)])
# elif prev_op == '-':
#     result -= int(s[prev_op_ind + 1: len(s)])     

# print(result) 


s = 'My heart in the Highland'
prev_ind = -1
for i in range(0, len(s)):
    if s[i] == ' ':
        print(s[prev_ind + 1: i])
        prev_ind = i

print(s[prev_ind + 1: len(s)])




