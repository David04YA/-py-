def reverse(s):
    return s[::-1]

def substr(s,x,y):
    return s[x:y]
# params:
#     s: 字符串
#     x: 开始下标
#     y: 结束下标


if __name__ == '__main__':
    print(reverse('123456'))
    print(substr('123456',1,3))