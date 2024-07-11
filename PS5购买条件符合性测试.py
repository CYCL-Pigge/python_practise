girlfirend_manner = input("你女朋友是否支持买PS5：")
wollet = input("你钱包是否宽裕：")
user_manner = input('你是否真的喜欢主机游戏：')
if girlfirend_manner == '是' and wollet == '是' and user_manner == '是':
    print('那就买它！')
elif girlfirend_manner == '否' and wollet == '是' and user_manner == '是':
    print('女朋友可能会打你，谨慎考虑')
else:
    print('没必要，放弃吧')