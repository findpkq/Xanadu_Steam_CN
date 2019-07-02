import re
import tkinter.filedialog
import tkinter.messagebox
import os,shutil,linecache
from tkinter import * 
from shutil import copyfile
from datetime import datetime


# 用于批量替换MadEdit无法正确转换的日文汉字
instead_target_path = 'F:/copy/Missing_Instead/'
missing_pattern = re.compile('{u\+\S{4}}',re.I)
#日志函数，用于记录未映射的汉字
def mylog(log_content):
    LogFile = open('Missing_' + datetime.now().date().isoformat() + '.txt', 'a')
    LogFile.write(log_content + '\n')
    LogFile.close()




def myKanji_Instead(rawfile):
    # 参考https://bbs.csdn.net/topics/392412615?page=1
    # 存为字典
    mydict = {}
    # cp932包含替换的奇葩汉字多于shift-jis
    with open("Missing_Kanji_Dictionary.txt",encoding = "utf-8", errors= 'ignore') as zidian:
        for a in zidian:
            # print(a)
            k = a.split()
            mydict[k[0]] = k[2]
    # print(mydict)
    # os.system('pause') 
    # FileA = 'F:/copy/Exchage_target/area00/MP_009d.scp'  
                

    path, filename = os.path.split(rawfile)
    name, extension = os.path.splitext(filename)

    # os.system('pause') 
    
    # 复制一份未替换脚本到当前文件夹
    shutil.copy(rawfile, path +  '/' + name + '_Instead' + extension)
    FileB = path +  '/' + name + '_Instead' + extension
    os.system('pause')
    # 执行替换
    with open(FileB,'r+',encoding = "ms932", errors= 'ignore') as pt:
        p = pt.read()
        for key,value in mydict.items(): 
            # print(value)
            p = p.replace(key,str(value)) 
        # print (p)
        pt.seek(0)
        pt.truncate()
        pt.write(p)

        # 检查剩余未映射汉字并输出
        mylog(filename)
        miss_result = missing_pattern.findall(p)
        # print(miss_result)
        print('\n'.join(miss_result))
        # mylog(str(miss_result))
        mylog('\n'.join(miss_result))
                

if __name__== '__main__':
    pfile = tkinter.filedialog.askopenfilename()
    # pfile_path = 'F:/copy/Exchage_target/'
    myKanji_Instead(pfile)
    os.system('pause') 