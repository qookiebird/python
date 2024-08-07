humanDict = {
    'age': 20, 'name' :'유현식', 'hobby':'독서',
    'address': {'city' :'seoul', 'gu' : '마포구', 'zipcode' : '12345'}
}
print(type(humanDict))
print(humanDict)

import json
humanString = json.dumps(humanDict,ensure_ascii=False, indent=4, sort_keys=True) # 사전을 문자열로 변환
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString)
print('이름 : %s' % humanJson['name'])
print('취미 : %s' % humanJson['hobby'])
print('나이 : %s' % humanJson['age'])
print('집코드 : %s' % humanJson['address']['zipcode'])
print('도시 : %s' % humanJson['address']['city'])
print('구 : %s' % humanJson['address']['gu'])