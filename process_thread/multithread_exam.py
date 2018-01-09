import threading            #1

#스레드에서 실행할 함수
def thread_main(li, i):     #2
    #range() 안의 값이
    #스레드가 담당할 리스트의 인덱스 범위를 결정
    for i in range(offset * i, offset *(i + 1)):  #3
        #요소에 2를 곱한다.
        li[i] *= 2

#리스트 요소의 개수
num_elem = 1000
#스레드의 개수
num_thread = 4
#오프셋 = 리스트 요수 개수 // 스레드 개수
#스레드 함수에서 연산을 담당한 인덱스 범위를 구하는데 쓰인다.
offset = num_elem // num_thread

li = [i+1 for i in range(num_elem)]

#스레드를 담을 리스트 
threads = []    #4
for i in range(num_thread):     #5
    #스레드 객체를 생성
    #target은 실행할 스레드 함수
    #args는 전달할 인자 목록
    th = threading.Thread(target = thread_main, args = (li, i))     #6
    threads.append(th)

for th in threads:
    #스레드 실행 시작
    th.start()      #7

for th in threads:
    #스레드 실행 완료 대기 
    th.join()       #8

print(li)

    
