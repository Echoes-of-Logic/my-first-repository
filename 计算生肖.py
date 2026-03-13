def ap():
  sx=['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
  year=int(input('请输入年份：'))
  print(year,"年是",sx[(year-2020)%12],"年")


def app():
  print('正在初始化列表…')
  sx=['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
  print('初始化成功！列表为',sx)
  year=int(input('请输入年份：'))
  print(year,"年是列表中的第",(year-2020)%12+1,"项，","为",sx[(year-2020)%12],"年。")


ap()
hd=input('输入Exit退出，输入Next继续运行\n请输入：')
if hd.lower() == "exit":
    exit()
elif hd.lower() == "next":
    print("开始运行二号程序")
    app()
    print("完毕")
    exit()
else:
    exit()
