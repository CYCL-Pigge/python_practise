game_list = ['黑神话：悟空' , '绝区零']
game_list.append('原神')
#.append 在列表中添加
game_list.remove('原神')
#.remove 在列表中删除
print(game_list)
print(len(game_list))
print(game_list[0])

game_list[0] = '原神'
print(game_list)

num_list = [0, -7, 10, 9]
print(num_list)
print(max(num_list))  #打印列表中最大值
print(min(num_list))  #打印列表中最小值
print(sorted(num_list))  #打印排序好的列表
print("=============")

#3-1
name = ['Eris', 'Dick', 'Maik']
print(len(name))
print(name[0])
print(name[1])
print(name[2])
print("=============")

#3-2
Hello = 'Nice to meet you'
print(f'{name[0]},{Hello}')
print(f'{name[1]},{Hello}')
print(f'{name[2]},{Hello}')
print("=============")

#3-4
dinner_invit = 'I want to invit you come for dinne with me'
print(f'{name[0]},{dinner_invit}')
print(f'{name[1]},{dinner_invit}')
print(f'{name[2]},{dinner_invit}')
print("=============")

#3-5
print('Dick can\'t go for dinner with me')
name[1] = 'Sarah'
print(f'{name[0]},{dinner_invit}')
print(f'{name[1]},{dinner_invit}')
print(f'{name[2]},{dinner_invit}')
print("=============")

#3-6
print('I find a bigger table')
name.insert(0, 'Wukong')
name.insert(2,'Anbi')
name.append('Bili')
print(f'{name[0]},{dinner_invit}')
print(f'{name[1]},{dinner_invit}')
print(f'{name[2]},{dinner_invit}')
print(f'{name[3]},{dinner_invit}')
print(f'{name[4]},{dinner_invit}')
print(f'{name[5]},{dinner_invit}')