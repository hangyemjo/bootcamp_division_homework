"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    year=int(input())
    month=int(input())

    if month in [4, 6, 9, 11]:
        print(30)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        print(31)
    else:
        if year%4==0 and year%100!=0:
            print(29)
        elif year%400==0:
            print(29)
        else:
            print(28)
    return


if __name__ == '__main__':
    main()
