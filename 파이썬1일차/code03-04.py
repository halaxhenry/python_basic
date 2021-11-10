sel = int(input("진수 타입을 넣으시오(16/10/8/2)"))
num = input('값 입력:')

if sel == 16:
    num16 = int(num)
    print(hex(num16))

if sel == 10:
    num10 = int(num)
    print(num10)

if sel == 8:
    num8 = int(num)
    print(oct(num8))


if sel == 2:
    num2 = int(num)
    print(bin(num2))
