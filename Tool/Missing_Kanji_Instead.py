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

# 复制函数
def mycopy1(filename,rawfile_path, target_fold):
    
    # print(os.path.exists(mydir+target_dir))
    if (os.path.exists(instead_target_path + '/' + target_fold)):
        pass
    else:
        os.makedirs(instead_target_path + '/' + target_fold)
        print(target_fold+' now create!')
    shutil.copy(rawfile_path, instead_target_path + '/' + target_fold + '/' + filename)

def myKanji_Instead(file_path):
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
                
    for root, dirs, files in os.walk(file_path):
        for ii in files:
            try:
                print(ii)
                FileA = root+"\\"+ii
                cnpath,filename=os.path.split(FileA)
                foldname = re.search('[^/]+(?!.*/)',cnpath)
                # print(foldname.group())
                # os.system('pause') 
                
                # 复制一份未替换脚本到目标文件夹
                mycopy1(filename, file_path + '/' +foldname.group()+ '/' +filename, foldname.group())
                FileB = instead_target_path + '/' + foldname.group() + '/' + filename
                print(filename)
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
                
            except Exception as err:
                continue
    # print("d")

if __name__== '__main__':
    # pfile_path = tkinter.filedialog.askdirectory()
    pfile_path = 'F:/copy/Exchage_target/'
    myKanji_Instead(pfile_path)
    os.system('pause') 