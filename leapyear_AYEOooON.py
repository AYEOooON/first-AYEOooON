if year <= 0:
    print('양의 정수를 입력하세요')
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print(str(year)+"년은 윤년입니다.")
            else:
                print(str(year)+"년은 평년입니다.")
        else:
            print(str(year)+"년은 윤년입니다.")
    else:
        print(str(year)+"년은 평년입니다.")
