import random

answer = random.randint(1,100)
print('정답 : %d' % answer)

counter = 0 # 카운터변수
while True:
    su = int(input('1부터 100사이의 정수 1개 입력 : '))

    counter += 1

    if answer > su:
        print('%d보다 큰 수를 입력해 주세요.' % su)
        pass
    elif answer < su:
        print('%d보다 작은 수를 입력해 주세요.' % su)
        pass
    else:
        print('정답입니다 나이스샷.')
        break
    #     end if
    # end while

    print('%d번만에 맞추었습니다.' % counter)