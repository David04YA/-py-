# a模式 追加内容 文件不存在也会创建文件
f=open("test.txt","a",encoding="utf-8")
f.write("\n黑马程序员")
f.flush()
f.close()   
# 追加内容 不会清空文件内容
