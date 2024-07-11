num_list = [0, 10, 2, 3, 9, 7, 12, 1234]
for num in num_list:
    if num > 2:
        print(f'{num}比2大')

#4-1练习
pizza_list = ['水果披萨', '奥尔良披萨', '榴莲披萨']
for pizza in pizza_list:
    print("我喜欢" + pizza)
print('我真的喜欢披萨!!')
print('==============')

#range 表示整数列
total = 0
for result in range(1, 101):
    total = total + result
print(total)
print('==============')

#4-4
num2_list = []
for i in range(1,1000001):
    num2_list.append(i)
# for i in num2_list:
#     print(i)
print('==============')

#4-5
print(min(num2_list))
print(max(num2_list))
print(sum(num2_list))