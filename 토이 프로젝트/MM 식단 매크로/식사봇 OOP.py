import requests
import datetime
import time
import json

class Meal:
    def __init__(self, num):
        self.cookies = {
            'remember-me': 'Y2pzcmhkODgyOjI2MjA1NDA3OTM2NTY6NzIwM2RkMzY1YzNhMWQ4MGE4NzRhOTNkYjJiN2FkOTY',
        }
        self.params = {
            'menuDt': datetime.datetime.today().strftime("%Y%m%d"),
            'menuMealType': num,
            'restaurantCode': 'REST000213',
        }
        
    def get_meal(self):
        response = requests.get('https://welplus.welstory.com/api/meal', params=self.params, cookies=self.cookies)
        return json.loads(response.text).get('data').get('mealList')

class UploadTime:
    def __init__(self, period):
        self.period = period
        
    def upload(self):
        count_time = time.perf_counter()
        count_menu = 0
        while True:
            count_time = time.perf_counter()
            now = int(datetime.datetime.now().strftime('%H'))
            if now >= 17: 
                meal = Meal(3)
                while True:
                    result = self.print_meal(meal, [0, 1, 4])
                    if result:
                        print('저녁이 출력되었습니다.')
                        break
                break
            elif count_menu == 0 and now >= 11: 
                count_menu += 1
                meal = Meal(2)
                while True:
                    result = self.print_meal(meal, [0, 1])
                    if result:
                        print('점심이 출력되었습니다.')
                        break
                continue
            else:
                print(f'{self.period}초 후에 재탐색합니다.')
                if self.period > time.perf_counter() - count_time:
                    time.sleep(self.period - time.perf_counter() + count_time)
                    
    def print_meal(self, meal, num):
        for i in num:
            meal_dict = meal.get_meal()[i]
            print(meal_dict)
            try:
                title = meal_dict.get("menuMealTypeTxt") 
                menu_name = meal_dict.get('subMenuTxt')
                kcal = meal_dict.get('kcal')
                photo_url = meal_dict.get('photoUrl') + meal_dict.get('photoCd')
                course = meal_dict.get('courseTxt')
                menu_print(title, menu_name, kcal, photo_url, course)
                return True
            except:
                pass
def menu_print(title, menu_name, kcal, photo_url,course):
    url = 'https://meeting.ssafy.com/hooks/e6qs4hmou7nxpm5e1x66xddjnh' # 서지호 - 연구소
    # url_1 = 'https://meeting.ssafy.com/hooks/jmikd999yigfzxj53i7y7xtz3e' # 서지호 - 구미 3반
    # url_2 = 'https://meeting.ssafy.com/hooks/nuu3ao3nb3dzixzmpm44m1pn7r' # 서지호 - 구미 전체 캠
    values = '{ "username": "Menu-Bot","text": "### ' + title + ' ' + course + '  :___nyamnyamgood_zoom:' + '\n' + menu_name +' '+ kcal + ' kcal\n![음식사진]('+photo_url+')"}'
    response = requests.post(url, data=values.encode('utf-8'))
    # response = requests.post(url_1, data=values.encode('utf-8'))
    # response = requests.post(url_2, data=values.encode('utf-8'))
    
upload_time = UploadTime(5)
upload_time.upload()
