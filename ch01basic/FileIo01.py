# FileIo01.py

print('파일에 기록합니다.')

# 절대 경로로 파일을 열거나 현재 작업 디렉토리를 확인하십시오.
myfile01 = open('mem.txt', mode='w', encoding='UTF-8')
print(type(myfile01))

members = ['홍영식', '김민수', '박수빈', '채수빈']

for mem in members:
    message = '\'%s\'님 안녕하세요.\n' % mem
    myfile01.write(message)  # 세미콜론은 생략 가능합니다.

myfile01.close()

print('기존 파일에 추가합니다')

# 파일을 append 모드로 열기
myfile02 = open('mem.txt', mode='a', encoding='UTF-8')

new_members = ['신유빈', '김진호', '모모노기카나']

for idx in range(len(new_members)):
    message = '%d번째 고객님 : %s님\n' % (idx + 1, new_members[idx])
    myfile02.write(message)  # 여기에 myfile02를 사용해야 합니다.

myfile02.close()

print('with 구문을 사용하면, close() 함수를 사용하지 않아도 됩니다.')
with open('test.txt', mode='w', encoding='UTF-8') as testfile:
    testfile.write('가나다\n')
    testfile.write("가나다\n")
    testfile.write("가나다\n")

    print('hello world', file=testfile)
