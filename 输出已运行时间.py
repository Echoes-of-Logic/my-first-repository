import time

sec:int = 1  #second
min:int = 0  #minute

#重复输出以运行时间
while True:
    time.sleep(1)
#不满1分钟就不显示分
    if min < 1:
        print(sec,"秒",end='\r')  #光标重头开始
    else:
        print(min,"分，",sec,"秒",end='\r')

    if sec ==59:
        sec = 0
        min +=1
    else:
        sec+=1
