# _*_ coding: utf-8 _*_

import requests
import datetime

def todaymenu(time):
    # now = datetime.datetime.today().strftime("%Y%m%d") # 오늘 날짜 코드
    now = datetime.date(2023, 1, 25).strftime("%Y%m%d") # 지정 날짜 코드
    cookies = {
        'remember-me': 'Y2pzcmhkODgyOjI2MjA1NDA3OTM2NTY6NzIwM2RkMzY1YzNhMWQ4MGE4NzRhOTNkYjJiN2FkOTY',
    }
    params = {
        'menuDt': now,
        'menuMealType': time,
        'restaurantCode': 'REST000213',
    }
    response = requests.get('https://welplus.welstory.com/api/meal', params=params, cookies=cookies)

    menulist = list(response.text.split('"'))
    count = []
    for menu in range(len(menulist)):
        if menulist[menu] == 'subMenuTxt':
            count.append(menulist[menu + 2])
    result = '\nA코너 메뉴 : '
    if time == '2':
        result += count[0]
        result += '\nC코너 메뉴 : '
        result += count[1]
    elif time == '3':
        result += count[0]
        result += '\nB코너 메뉴 : '
        result += count[1]
        result += '\nTAKE OUT : '
        result += count[4]
    return result


if __name__ == "__main__":
    url = 'https://meeting.ssafy.com/hooks/xejboqkqr3n6zkdkke3k633jiw'

    headers = {'Content-Type': 'application/json', }
    menu_1 = todaymenu('2')
    menu_2 = todaymenu('3')
    # # (f'http://samsungwelstory.com/data/manager/recipe/E21F/{now}/') # 식사 이미지 아이콘 링크
    values = '{ "icon_url": "http://samsungwelstory.com/data/manager/recipe/E21F/20230119/","username": "Menu-Bot","text": "### 오늘 점심 메뉴\n'+ menu_1 +'\n ### 오늘 저녁 메뉴\n'+ menu_2 +'"}'
    response = requests.post('https://meeting.ssafy.com/hooks/e6qs4hmou7nxpm5e1x66xddjnh', data=values.encode('utf-8'))
