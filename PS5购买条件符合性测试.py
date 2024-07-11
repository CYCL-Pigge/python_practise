girlfriend_manner = input("你女朋友是否支持买PS5（是/否）：")
wallet = input("你钱包是否宽裕（是/否）：")
user_manner = input('你是否真的喜欢主机游戏（是/否）：')

if user_manner == '是' and wallet == '是':
    if girlfriend_manner == '是':
        print('那就买它！')
    else:
        print('女朋友可能会打你，谨慎考虑')
else:
    print('没必要，放弃吧')
