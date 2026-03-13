st:str=None
end=""

st=str(input('请输入字符：'))
print(len(st),"个字符")
for i in st:
    print(i)
    end=i+end
print(end)
