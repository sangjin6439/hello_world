print("1.+ \n2.- \n3.* \n4./ \ne.나가기 \nc.다시입력")

while True:
    a =  int(input("기능을 선택하시오."))
    if(a <= 5):
        number1 = int(input("첫번째 숫자 입력."))
        number2 = int(input("첫번째 숫자 입력."))
        if(a == 1):
            print("계산결과: %d "%(number1 + number2))
        elif (a == 2):
            print("계산결과: %d " % (number1 - number2))
        elif (a == 3):
            print("계산결과: %d " % (number1 * number2))
        elif (a == 4):
            print("계산결과: %d " % (number1 / number2))
        elif (a == e):
            break
        elif (a == c):
            continue
        else:
             print("다시 입력해 주세요.")
