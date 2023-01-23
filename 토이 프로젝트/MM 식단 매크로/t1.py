import requests

cookies = {
    'remember-me': 'Y2pzcmhkODgyOjI2MjA1NTY1Mzg1MTA6NTQ4NGFmNWVlNmU1OTU2OTEyMDg4OTIzYmJlMjJjNDY',
}

params = {
    'menuDt': '20230125',
    'menuMealType': '2',
    'restaurantCode': 'REST000213',
    'sortingFlag': 'ai',
}

response = requests.get('https://welplus.welstory.com/api/meal', params=params, cookies=cookies)


def prase_json(response):
    json_object = response.json()

    menu_data = {}
    lunch_a = []
    lunch_b = []
    meal_list = json_object.get('data').get('mealList')
    for data in meal_list:
        menu_course_type = data.get('menuCourseType')
        menu_txt = data.get('subMenuTxt')

        if menu_course_type == 'AA':
            lunch_a = menu_txt.split(',')
        elif menu_course_type == 'BB':
            lunch_b = menu_txt.split(',')

    menu_data['A코너'] = lunch_a
    menu_data['B코너'] = lunch_b

    return menu_data

a = print(prase_json(response))

headers = {}
values = '{*a}'
response = requests.post('https://meeting.ssafy.com/hooks/e6qs4hmou7nxpm5e1x66xddjnh', headers=headers, data=values) 