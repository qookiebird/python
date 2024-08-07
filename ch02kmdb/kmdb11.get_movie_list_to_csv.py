import urllib.request
import urllib.parse
import json, math

#블라블라블라 아라라라라리요
#해당 사이트에서 발급받은 키
#아라랄랄라랄라
#다다다다다다다다 와 다다다다다다다다
service_key ='41e3ac0a61bc585e45c4895e3f9bc484'

def getDataFromWeb(url):
    #url 정보를 이용하여 해당 웹 사이트에서 json 데이터를 읽어 옵니다.
    req = urllib.request.Request(url) #요청객체
    try:
        response = urllib.request.urlopen(req) #응답객체
        # http 응답코드가 성공이면 200을 반환합니다.
        if response.getcode()== 200:
            #바이트 타입을 문자열로 반환하여 변환합니다.
            return response.read().decode('UTF-8')
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return  None
# end def getDataFromWeb


def movieExtractor(pageNumber, pageSize, thisYear):
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'

    parameter = '?key=' + service_key
    parameter += '&curPage=' + str(pageNumber)
    parameter += '&itemPerPage=' + str(pageSize)
    parameter += '&openStartDt=' + str(thisYear)

    movie_name = '행복의나라'
    encoded_movie_name = urllib.parse.quote(movie_name, encoding='UTF-8')
    parameter += '&movieNm=' + encoded_movie_name


    url = end_point + parameter
    # print(url)

    jsonData = getDataFromWeb(url)

    if jsonData == None :
        return None
    else:
        try:
           return json.loads(jsonData)
        except Exception as err:
            print('JSON 데이터에 문제가 있습니다.')
            print(err)
            return None

        # end try
    #end if
#end def movieExtractor



import pandas as pd

#영화 정보를 저장할 데이터 프레임
movieTable = pd.DataFrame()



def makeMovieTable(movieData):
    for onemovie in movieData['movieListResult']['movieList']:
        # print(onemovie['movieCd'])
        onedict = {
            'movieCd': onemovie['movieCd'],
            'movieNm': onemovie['movieNm'],
            'movieNmEn': onemovie['movieNmEn'],
            'prdtYear': onemovie['prdtYear'],
            'openDt': onemovie['openDt'],
            'typeNm': onemovie['typeNm'],
            'prdtStatNm': onemovie['prdtStatNm'],
            'nationAlt': onemovie['nationAlt'],
            'genreAlt': onemovie['genreAlt'],
            'repNationNm': onemovie['repNationNm'],
            'repGenreNm': onemovie['repGenreNm'],
            'directors': str(onemovie['directors']),
            'companys': str(onemovie['companys'])
        }
        # print(onedict)

        oneframe = pd.DataFrame(onedict,index=[0])
        # print(oneframe)

        global movieTable #전역 변수임을 알리기 위하여 global 키워드를 사용합니다.
        #이번에 생성된 데이터 프레임 oneframe을 movieTable에 누적시킵니다.
        movieTable = pd.concat([movieTable, oneframe])
        # print('-')


# end def getDataFromWeb

print('크롤링 중입니다. 잠시만 기다려 주세요.')

startYear, endYear = 2024, 2025
pageSize = 100 #최대 100개까지 가능

for thisYear in range(startYear, endYear):
    print('%s년도 크롤링중입니다.' % thisYear)
    pageNumber = 1

    while True:
        movieData = movieExtractor(pageNumber,pageSize,thisYear)
        # print(movieData)
        try:
            totCnt = movieData['movieListResult']['totCnt']

        except Exception as err:
            # 이번 페이지에 존재하지 않으면 다음 페이지로 넘어 가세요.
            pageNumber +=1
            continue

        if pageNumber ==1: # 1페이지 일때만 전체 개수를 출력합니다.
            print('데이터 총 개수 : ' + str(totCnt))

        if totCnt ==0: # 0이면 더이상 존재하지 않는 것으로 간주합니다.
            break

        totalPage = math.ceil(totCnt/pageSize)
        print('진행 중인 페이지: ' + str(pageNumber) + '/' + str(totalPage))

        makeMovieTable(movieData)

        if pageNumber == 10:
            break

        pageNumber += 1



print('크롤링이 끝났습니다.')
print(movieTable)
print(type(movieTable))
print(movieTable.info())

#CSV(comma separate value) : 텍스트 형식의 파일로 엑셀에서 열 수 있습니다.
filename = 'kmdb_get_movie_list_csv'
movieTable.to_csv(filename,index=False,encoding='UTF-8')
print(filename + '파일이 저장되었습니다.')


# movieExtractor(1,100,None)
