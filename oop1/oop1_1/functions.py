import openpyxl
import math

def average(scores):
    s = 0
    for score in scores:
        s += score
    return round(s/len(scores), 1)

def variance(scores, avrg):
    s= 0
    for score in scores:
        s += (score - avrg) ** 2
    return round(s/len(scores), 1)

def std_dev(variance):
    return round(math.sqrt(variance),1)

def get_data_from_excel(filename):
    '''
    get_data_from_excel(filename) -> {'name1' : 'score1', 'name2' : 'score2', ....}
    엑셀 파일에서 데이터를 가져옵니다.
    반환 값은 key가 학생 이름이고 value가 점수인 딕셔너리입니다. 
    '''
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows

    for name, score in g:
        dic[name.value] = score.value

    return dic

def evaluateClass(avrg, total_avrg, std_dev, sd):
    '''
    evaluateClass(avrg, total_avrg, std_dev, sd) -> None
    avrg : 반 성적 평균
    total_avrg : 학년 전체 성적 평균
    std_dev : 반의 표준 편차
    sd : 원하는 표준 편차 기준
    '''
    if avrg <total_avrg and std_dev >sd:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > total_avrg and std_dev >sd:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < total_avrg and std_dev <sd:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > total_avrg and std_dev <sd:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

#만약 이 파일을 메인으로 실행 : if 문 아래가 실행
#모듈로 임포트 되는 경우 : if 문 아래가 실행 안됨
#라이브러리일 때 : 테스트 코드

if __name__ == "__main__":
    li = [3, 5, 6, 8, 2]
    avrg = average(li)
    print(avrg)
    











