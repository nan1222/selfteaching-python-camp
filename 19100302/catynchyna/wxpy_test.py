#encoding=utf-8
# Created by double lin at 2018/8/16
'''
from wxpy import *
 
bot = Bot(cache_path=True, console_qr=False)
# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')
 
friends = bot.friends()
sex_male = 0
sex_femal = 0
unkown = 0
for i in range(len(friends)):
    print ('friends[i]:\t', friends[i])  # 聊天对象格式为：<Friend: 备注名称>
    print ('nick_name:\t' + friends[i].nick_name ) # 微信好友的微信昵称
    print ('name:\t' + friends[i].name )  # 扫码用户对该微信好友的备注
    print ('remark_name:\t' + friends[i].remark_name)
    print ('bot:\t', friends[i].bot)    # 机器人对象 格式为：<Bot: 备注名称>
    print ('raw:\t', friends[i].raw)    # 微信好友对应的用户详细信息json数据
    print ('puid:\t' + friends[i].puid)   # 微信好友对应的puid值
    print ('NickName:\t' + friends[i].raw['NickName'])  # 打印备注信息
    print ("Province:\t" + friends[i].raw['Province'])    # 打印好友所在的省份
    # print friends[i].province
    print ("City:\t\t\t" + friends[i].raw['City'])    # 城市
    # print friends[i].city
    # 男性 sex值为1， 女性值为2 未提供为0
    print (friends[i].raw['Sex'],)
    if friends[i].raw['Sex'] == 1:
        sex_male += 1
    elif friends[i].raw['Sex'] == 2:
        sex_femal += 1
    else:
        unkown += 1
print ('count of male is:', sex_male, 'count os female is:', sex_femal,'不知道性别的共:', unkown)
print ('共有好友:', len(friends))
'''

#encoding=utf-8
from wxpy import *
 
bot = Bot(cache_path=True)
 
# 找到好友列表中昵称为“我说”的好友，监控聊天，打印该好友发来的文本消息
myfriend = bot.friends().search(u'我')[0]
@bot.register(myfriend, TEXT)
def print_msg1(msg1):
    print(msg1)
 
#监控群聊消息，打印群聊中的文本消息
@bot.register(Group, TEXT)
def print_msg(msg):
    print (msg)
 
bot.join()
