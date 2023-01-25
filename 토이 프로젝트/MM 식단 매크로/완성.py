# _*_ coding: utf-8 _*_

import requests
import datetime
import time
import json

# --------------------------------------------------
period = 5  # 탐색 주기(초)
# --------------------------------------------------
lunch = 2 # access_key(2)
dinner = 3 # access_key(3)
def upload_time():
    count_time = time.perf_counter()
    count_menu = 0
    while True:
        count_time = time.perf_counter()
        if int(datetime.datetime.now().strftime('%H')) >= 17: # 17 시 넘었다면
        # if int(datetime.datetime.now().strftime('%M')) >= 37: # 분단위로 테스트용
            dinner_fun([0, 1, 4])
            break
        elif count_menu == 0:
            if int(datetime.datetime.now().strftime('%H')) >= 11: # 11 시 넘었다면
                count_menu += 1
                lunch_fun([0, 1])
                continue
        else:
            print(f'{period}초 후에 재탐색합니다.')
            if period > time.perf_counter() - count_time:
                time.sleep(period - time.perf_counter() + count_time)

def access_key(num):
    now = datetime.datetime.today().strftime("%Y%m%d") # 오늘 날짜 코드
    # print(now)
    # now = datetime.date(2023, 1, 20).strftime("%Y%m%d") # 지정 날짜 코드
    cookies = {
        'remember-me': 'Y2pzcmhkODgyOjI2MjA1NDA3OTM2NTY6NzIwM2RkMzY1YzNhMWQ4MGE4NzRhOTNkYjJiN2FkOTY',
    }
    params = {
        'menuDt': now,
        'menuMealType': num,
        'restaurantCode': 'REST000213',
    }
    response = requests.get('https://welplus.welstory.com/api/meal', params=params, cookies=cookies)
    menulist = json.loads(response.text)
    
    # print(menulist)
    return menulist

# 0, 1 점심 A, C 
def lunch_fun(num):
    for i in num:
        lunch_dict = access_key(lunch).get('data').get('mealList')[i]
        print(lunch_dict)
        title = lunch_dict.get("menuMealTypeTxt")
        menuname = lunch_dict.get('subMenuTxt')
        kcal = lunch_dict.get('kcal')
        photo_url = lunch_dict.get('photoUrl') + lunch_dict.get('photoCd')
        course = dinner_dict.get("courseTxt")
        menu_print(title, menuname, kcal, photo_url, course)

# 0, 1, 4 저녁 A, B, take_out
def dinner_fun(num):
    for i in num:
        # print(i)
        dinner_dict = access_key(dinner).get('data').get('mealList')[i]
        # print(dinner_dict)
        title = dinner_dict.get("menuMealTypeTxt")
        menuname = dinner_dict.get('subMenuTxt')
        kcal = dinner_dict.get('kcal')
        photo_url = dinner_dict.get('photoUrl') + dinner_dict.get('photoCd')
        course = dinner_dict.get("courseTxt")
        menu_print(title, menuname, kcal, photo_url, course)
# print(access_key)
# print(dinner([3,4,5]))


def menu_print(title, menuname, kcal, photo_url, course):
    url = 'https://meeting.ssafy.com/hooks/e6qs4hmou7nxpm5e1x66xddjnh' # 서지호 - 연구소
    # url = 'https://meeting.ssafy.com/hooks/jmikd999yigfzxj53i7y7xtz3e' # 서지호 - 구미 3반
    # url = 'https://meeting.ssafy.com/hooks/nuu3ao3nb3dzixzmpm44m1pn7r' # 서지호 - 구미 전체 캠
    # now = datetime.date(2023, 1, 20).strftime("%Y%m%d") # 지정 날짜 코드
    # headers = {'Content-Type': 'application/json', }
    values = '{ "username": "Menu-Bot","text": "### ' + course + ' '+ title + ' '+ kcal + ' kcal\n' + menuname +' \n![이미지테스트]('+photo_url+')\n"}'
    response = requests.post(url, data=values.encode('utf-8'))
#----------------------------------------------------------------------



if __name__ == "__main__":  
    upload_time()