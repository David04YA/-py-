def test(a,b):
    print(a+b)


if __name__=="__main__":
    test(1,2)
# 所有执行的代码都在if __name__=="__main__":  这个mode被引用时就不是主函数了
# 被引用时,__name__就是模块名
