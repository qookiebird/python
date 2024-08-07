filename = 'jumsu.json'

# rt는 텍스트 모드로 읽어 들입니다.
myfile = open(filename,mode='rt', encoding ='UTF-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

import json
jsonData  =json.loads(mystring)
print(type(jsonData))

humanList = list()  #전체 결과를 저장할 리스트

for human in jsonData:
    name = human['name']
    print('이름 :%s' % name)

    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

    _gender = human['gender'].upper()
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    if 'hello' in human.keys():
        message = human['hello']
        print('메시지 : ', message)
    #end if


    mytuple = (name,kor,eng,math,total,gender,message)
    humanList.append(mytuple)

print(humanList)





