'''
@Author: your name
@Date: 2019-11-17 22:03:18
@LastEditTime: 2019-11-18 00:08:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /learnpy/PythonNotes/demo/funtion.py
'''
# 返回完整的姓　名
def get_formatted_name(first_name, last_name, middle_name = ''):
    full_name = first_name + middle_name + last_name
    return full_name.title()

# musician = get_formatted_name(first_name = '杨', last_name = '永')
# musician2 = get_formatted_name(first_name = 'cock', last_name='roach', middle_name='basec')
# print(musician2)
# print(musician, format('是个好同志'))


# 利用字典编写猜专辑歌名游戏
# 啊桑两张专辑，任意选择一张专辑进行游戏，猜对一张专辑内的４首歌以上获得红包奖励;


def make_album(special_name, username, song_name = ''):
    game_data = {
        'name' : username,
        'special' : special_name,
        'song' : []
    }

    
    # game_data['song'].append(song_name)
    
    test = len(game_data['song'])
    game_data['len'] = test
    
    return game_data

special_a = ('叶子', '杯子', '痞子')
special_b = ('寂寞', '唱歌', '嗓子')

while True:
    name = input('输入您的姓名:')
    special = input('输入专辑名称:')
    
    if  special == 'special_a':
        for  itmes in special_a:
            song = input('输入歌曲名称:')
            if song == itmes:
                song_data = []
                song_data.append(song)

                print(song_data)

    elif special == 'special_b':
        for itmes in special_b:
            song = input('输入歌曲名称:')
            if  song == itmes:
                print('yes')
            else:
                print('错误！')
                break
    else:
        print('输入错误！')

    result = make_album(special_name = special, song_name = song_data, username=name)

    print(result)
