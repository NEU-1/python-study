# _*_ coding: utf-8 _*_

from urllib import request # 사진
from PIL import Image # 사진
from io import BytesIO # 사진
import requests
import datetime
import time

# --------------------------------------------------
period = 5  # 탐색 주기(초)
# --------------------------------------------------

def picture():
    url = 'https://item.kakaocdn.net/do/f26523b6d699852ace4f3c49f086f7a4617ea012db208c18f6e83b1a90a7baa7'

    res = request.urlopen(url).read()
    img = Image.open(BytesIO(res))
    return img
print(picture())


def menuprint():
    url = 'https://meeting.ssafy.com/hooks/xejboqkqr3n6zkdkke3k633jiw'

    now = datetime.date(2023, 1, 20).strftime("%Y%m%d") # 지정 날짜 코드
    headers = {'Content-Type': 'application/json', }
    menu_1 = todaymenu('2')
    menu_2 = todaymenu('3')
    global picture
    picture = picture()
    # # (f'http://samsungwelstory.com/data/manager/recipe/E21F/{now}/') # 식사 이미지 아이콘 링크
    values = '{ "username": "Menu-Bot","text": "### 오늘 점심 메뉴\n' + menu_1 + '\n ### 오늘 저녁 메뉴\n' + menu_2 + '\n", picture}'
    response = requests.post('https://meeting.ssafy.com/hooks/e6qs4hmou7nxpm5e1x66xddjnh', data=values.encode('utf-8'))

def todaymenu(time):
    # now = datetime.datetime.today().strftime("%Y%m%d") # 오늘 날짜 코드
    now = datetime.date(2023, 1, 20).strftime("%Y%m%d") # 지정 날짜 코드
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

def main():
    count_time = time.perf_counter()
    while True:
        count_time = time.perf_counter()
        if int(datetime.datetime.now().strftime('%H')) >= 11: # 11 시 넘었다면
        # if int(datetime.datetime.now().strftime('%M')) >= 37: # 분단위로 테스트용
            menuprint()
            break
        else:
            print(f'{period}초 후에 재탐색합니다.')
            if period > time.perf_counter() - count_time:
                time.sleep(period - time.perf_counter() + count_time)

if __name__ == "__main__":
    main()