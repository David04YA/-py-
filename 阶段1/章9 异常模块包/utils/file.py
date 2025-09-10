def file_info(file_name):
    """
    param file_name: 即将读取的文件路径
    return: None
    """
    f = None
    try:
        f = open(file_name, 'r',encoding='utf-8')
        content = f.read()
        print(content)
    except FileNotFoundError:
        print('文件不存在')
    finally:
        if f:  #如果变量是None 与false等同，如果不是None 与true等同
            f.close()

# 示例调用
# file_info('test.txt')

if __name__ == '__main__':
    file_info(r'C:\Users\26705\Desktop\IDE\py黑马\test.txt')  # 修复：使用原始字符串


def append_file(file_name,content):
    """
    param file_name: 即将写入的文件路径
    param content: 即将写入的内容
    return: None
    """
    f = open(file_name,'a',encoding='utf-8')
    f.write(content)
    f.close()

if __name__ == '__main__':
    append_file(r'C:\Users\26705\Desktop\IDE\py黑马\test.txt','这是追加的内容')