# 通过文本操作，读取此文件，统计itheima单词出现的次数
f=open("课件/word.txt","r",encoding="utf-8")
# 1.read()然后count()
content=f.read()
count=content.count("itheima")
print(count)
# 2.一行行读取文件 按照空格切分 统计itheima单词出现的次数
count=0
for line in f:
    line=line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1

print(count)


f.close()