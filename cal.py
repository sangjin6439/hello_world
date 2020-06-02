file = open("hi",'w')

def sum(n1,n2):
   return n1+n2
def min(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

print("1.더하기  2.빼기  3.곱하기  4.나누기  5.종료\n")

while True:
    a = int(input("기능을 선택하십시오. "))
    if(a <= 4):
        n1 = int(input("첫번째 숫자 입력"))
        n2 = int(input("두번째 숫자 입력"))

        if(a == 1):
            be = sum(n1, n2)
            print("결과: %d" % be)
            file.write("%d\n"%be)


        elif(a == 2):
            be=min(n1, n2)
            print("결과: %d" % be)
            file.write("%d\n" % be)


        elif(a == 3):
            be=mul(n1,n2)
            print("결과: %d" % be)
            file.write("%d\n" % be)

        elif(a == 4):
            be=div(n1,n2)
            print("결과: %d" % be)
            file.write("%d\n" % be)

    elif(a == 5):
            break
    else:
        print("다시 입력해주십시오")
file.close()


