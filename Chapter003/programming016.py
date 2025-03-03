n = input("글자 입력 : ")
msg = ""

if (n>='0' and n<='F') :
    if (n >= '0' and n <= '1'):
        msg += "2진수"
    if (n >= '0' and n <= '7'):
        if(len(msg)!=0) : msg += " 또는 "
        msg += "8진수"
    if (n >= '0' and n <= '9'):
        if(len(msg)!=0) : msg += " 또는 "
        msg += "10진수"
    if (n >= '0' and n <= 'F'):
        if(len(msg)!=0) : msg += " 또는 "
        msg += "16진수"
    msg += " 입니다"
else :
    msg += "숫자가 아닙니다."

print(msg)