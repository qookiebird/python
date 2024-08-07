def sungjukInfo(name, kor, eng, math):
    total = kor + eng + math
    average = total / 3.0

    if average >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'

    print('%s 학생의 정보' % name)
    print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
    print('총점 : %d, 평균 : %.2f, 합격여부 : %s' % (total, average, passOrFail))

# 김철수의 성적 정보
name, kor, eng, math = '김철수', 50, 60, 70
sungjukInfo(name, kor, eng, math)  # positional argument

# 박영희의 성적 정보 - 점수 입력 추가
sungjukInfo('박영희', 80, 90, 85)  # 이제 4개의 인자를 전달

# 쿠키의 성적 정보
sungjukInfo(math=30, eng=90, name='쿠키', kor=100)

# 하하하의 성적 정보 - 점수 입력 추가
sungjukInfo('하하하', 50, math=30)   # 이제 4개의 인자를 전달