def para_func(v1, v2, v3=0):
    result = 0
    result = v1 + v2 + v3
    return result


hap = 0

hap = para_func(10, 20)
print(f"매개변수가 2개인 함수를 호출한 결과 ==> {hap}")
hap = para_func(10, 20, 30)
print(f"매개변수가 3개인 함수를 호출한 결과 ==> {hap}")


def para_func_1(v1=10, v2=30):
    result = v1 / v2
    return result


hap = para_func_1()
print(hap)


hap = para_func_1(v2=40, v1=10)
print(hap)
