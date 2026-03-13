#编码与解码（编码：ord）（解码：chr）

def d_ord():     #编码的函数
    v_ord = input('请输入需要编码的内容：')
#    print(type(v_ord)) #调试用
    print(ord(v_ord))

def d_chr():     #解码的函数
    v_chr = input('请输入需要解码的内容：')
#    print(type(v_chr)) #调试用
    v_chr = int(v_chr)
#    print(type(v_chr)) #调试用
    print(chr(v_chr))

while True:
    zt = input('输入：')
    if zt=='编码' or zt=="b":
        d_ord()
    elif zt=='解码' or zt=='j':
        d_chr()
    else:
        input('Exit')
        break
        exit()
