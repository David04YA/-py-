# 直接调用write()方法写入内容 然后调用flush()方法刷新缓冲区

f=open("test.txt","w",encoding="utf-8")
f.write("hello world")

f.flush()
f.close()

# write会把内容清空，写入新的内容