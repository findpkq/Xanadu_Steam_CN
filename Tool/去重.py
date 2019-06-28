import shutil
readPath='Missing_2019-06-26.txt'
writePath='fix2.txt'
lines_seen=set()
outfiile=open(writePath,'a+')
f=open(readPath,'r')
for line in f:
    if line not in lines_seen:
        outfiile.write(line)
        lines_seen.add(line)
# --------------------- 
# 作者：TtingZh 
# 来源：CSDN 
# 原文：https://blog.csdn.net/t_zht/article/details/83377165 
# 版权声明：本文为博主原创文章，转载请附上博文链接！