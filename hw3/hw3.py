print('Задача 16')
print('Введите размер массива и его элементы')
numbers = [int(input()) for _ in range(int(input()))]
print('Введите искомое число')
n = int(input())

counter = 0
 
for i in range(len(numbers)):
    if numbers[i] == n:
        counter += 1

print(f'В массиве {numbers}')
print(f'число {n} встречается {counter} раз.')
print()
 

#---------------------------------------

print('Задача 18')
print('Введите размер массива и его элементы')
numbers = [int(input()) for _ in range(int(input()))]
print('Введите искомое число')
n = int(input())

min_distance = abs(n - numbers[0])
index = 0

 

for i in range(1, len(numbers)):

    distance = abs(n - numbers[i])

    if distance < min_distance:

        min_distance = distance

        index = i

 

print(f'В массиве {numbers}')

print(f'наиболее близкий к числу {n} элемент a[{index}] = {numbers[index]} .')

 