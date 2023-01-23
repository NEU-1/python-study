import requests
import pprint

cookies = {
    'WCPCID': 'a738d10d-fd6e-4011-5bcb-e903e64c3efe-1674459009822',
    'introNoShow': 'N',
    'cafeteriaActiveId': 'REST000213',
    'cafeteriaActiveName': '^%^EC^%^A0^%^84^%^EC^%^9E^%^90^%^EA^%^B5^%^AC^%^EB^%^AF^%^B82^%^EC^%^BA^%^A0^%^ED^%^8D^%^BC^%^EC^%^8A^%^A43^%^EC^%^8B^%^9D^%^EB^%^8B^%^B9',
    'JSESSIONID': 'jLTd58hoWnfj0U5LxncFe23s0dYESZ9XVc0c8su2qPsZMzqXNei6^!558439737^!-1870908805',
    'remember-me': 'Y2pzcmhkODgyOjI2MjA1NDUyMzMwMDI6NDdmNTc1M2E5ZDIxYWE3NWZiN2U4NTRjMmQzYjk3OWQ',
    'UID': 'cjsrhd882',
    'PCID': 'Z00000253974',
    'mealDate': '20230125',
    'daysActiveDate': '01.25',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://welplus.welstory.com/',
    # 'Cookie': 'WCPCID=a738d10d-fd6e-4011-5bcb-e903e64c3efe-1674459009822; introNoShow=N; cafeteriaActiveId=REST000213; cafeteriaActiveName=^%^EC^%^A0^%^84^%^EC^%^9E^%^90^%^EA^%^B5^%^AC^%^EB^%^AF^%^B82^%^EC^%^BA^%^A0^%^ED^%^8D^%^BC^%^EC^%^8A^%^A43^%^EC^%^8B^%^9D^%^EB^%^8B^%^B9; JSESSIONID=jLTd58hoWnfj0U5LxncFe23s0dYESZ9XVc0c8su2qPsZMzqXNei6^!558439737^!-1870908805; remember-me=Y2pzcmhkODgyOjI2MjA1NDUyMzMwMDI6NDdmNTc1M2E5ZDIxYWE3NWZiN2U4NTRjMmQzYjk3OWQ; UID=cjsrhd882; PCID=Z00000253974; mealDate=20230125; daysActiveDate=01.25',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'menuDt': '20230125',
    'menuMealType': '3',
    'restaurantCode': 'REST000213',
    'sortingFlag': 'ai',
}

response = requests.get('https://welplus.welstory.com/api/meal', params=params, cookies=cookies, headers=headers)
a = list(response.text.split('"'))
count = []
for i in range(len(a)):
    if a[i] == 'subMenuTxt':
        count.append(a[i+2])
print(count[0], count[1], count[4])
