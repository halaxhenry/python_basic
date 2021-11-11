def func1():
    result = 100
    return result


def func2(x):
    print(f"func2()의 반환 값은 ==? {x}")


hap = 0

hap = func1()

print(f"func1() 에서 돌려준값 ==> {hap}")
func2(hap)
