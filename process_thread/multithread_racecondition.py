import threading

#모든 스레드가 공유할 데이터
g_count = 0             #1

#스레드가 실행할 함수
def thread_main():      #2
    global g_count

    for i in range(100000):
        g_count += 1

threads = []

for i in range(50):     #3
    th = threading.Thread(target = thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_count : {:,}'.format(g_count))     #4
    
