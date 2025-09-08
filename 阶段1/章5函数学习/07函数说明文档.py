# 函数添加说明文档，来辅助理解函数
def func(x,y):
    result = x + y
    """
    这是一个函数的说明文档
    :param x: 这是第一个参数
    :param y: 这是第二个参数
    :return: 这是返回值
    """
    print("两数相加的结果是%d" % result)
    return result
func(1,2)