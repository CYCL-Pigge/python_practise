message = " yo what up "
print(message.title())
#.title() 将句子中的首字母大写
print(message.upper())
#.upper() 将句子中所有字母大写
print(message.lower())
#.lowr() 将句子中字母全转换成小写
print(message.lstrip())
#.lstrip() 字符串开头不再有空格
print(message.rstrip())
#.rstrip() 字符串结尾不再有空格
print(message.strip())
#.strip() 字符串开头和结尾不再有空格
print(message.removeprefix(" yo"))
#.removeprefix() 移除字符串前缀
print(message.removesuffix("up "))
#.removesuffix() 移除字符串后缀
num = "123"
message = f"{num}qq"
print(message)

#2-3
user_name = "Eris"
print(f"Hello {user_name},Would you like to learn some Python today?")
print("==============")
#2-4
print(user_name.lower())
print(user_name.upper())
print(user_name.title())
