# 异常有传递性,当所有函数都没有处理异常时,异常会传递到主函数,如果主函数也没有处理异常,那么程序就会崩溃


def func1():
    print("func1")
    num = 1/0
    func2()

def func2():
    print("func2")
    func1()


def main():
    try:
        func2()
    except Exception as e:
        print("出现了未知异常")

main()