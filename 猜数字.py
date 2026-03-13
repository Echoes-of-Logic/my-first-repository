import random as r    #导入生成伪随机数模块

sj = r.randint(0,100)    #生成随机数
hd = int(input ('请输入数字：'))   #获取int类型的用户输入
cs = 10    #机会次数


#如果用户输入错误则继续
while hd != sj:    
    if hd > sj:
        print ("大了")
    if hd < sj:  #判断用户输入大还是小了
        print ("小了")
    if cs <= 1:
        print('机会用尽')
        break    #机会用尽就退出循环
    cs-= 1
    hd = int(input ('请输入数字：'))   #继续询问
else:
    print ('正确')  #如果用户输入正确就转到else
