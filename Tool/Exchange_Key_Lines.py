import re
import tkinter.filedialog
import tkinter.messagebox
import os,shutil,linecache
from tkinter import * 
from shutil import copyfile
from datetime import datetime

# 基于中文脚本文件出发，替换英文脚本中中涉及文本的行并另存至另一个文件夹

path_target = 'F:/copy/Exchage_target'

#日志函数记录出现的问题便于后续调整
def mylog(log_content):
    LogFile = open(datetime.now().date().isoformat()+'.txt', 'a')
    LogFile.write(log_content+'\n')
    LogFile.close()

# 复制函数
def mycopy1(filename,rawfile_path, target_fold):
    
    # print(os.path.exists(mydir+target_dir))
    if (os.path.exists(path_target + '/' + target_fold)):
        pass
    else:
        os.makedirs(path_target + '/' + target_fold)
        print(target_fold+' now create!')
    shutil.copy(rawfile_path, path_target + '/' + target_fold + '/' + filename)

def myExchage():
    path_CN = 'F:/copy/CN_Text_Exist_JIS_rename/'
    path_EN = 'F:/copy/new_En_Exist'
    # FileA = 'F:/copy/CN_Text_Exist_JIS_rename/area00/MP_00a0.scp'
    # 判断是否为显示文本相关脚本的正则表达式
    regex = re.compile('sys|sel\(|set_name|msg',re.I) 
    # if regex.findall('_ex("Greetings.",-1,4)') != []:
    #     print('find')
    # else:
    #     print('not find')
    # print(regex.findall('msg_ex("Greetings.",-1,4)'))
    for root, dirs, files in os.walk(path_CN):
        for ii in files:
            try:
                print(ii)
                FileA = root+"\\"+ii
                cnpath,filename=os.path.split(FileA)
                foldname = re.search('[^/]+(?!.*/)',cnpath)
                # print(foldname.group())
                # os.system('pause') 
                
                # 复制一份英文脚本到目标文件夹
                mycopy1(filename, path_EN + '/' +foldname.group()+ '/' +filename, foldname.group())
                FileB = path_target + '/' + foldname.group() + '/' + filename
                F1file = open(FileA, 'r', encoding='shift_jis', errors= 'ignore')
                F2file = open(FileB, 'r+', encoding='shift_jis', errors= 'ignore')
                f1 =  F1file.readlines()
                f2 =  F2file.readlines()
                countA = len(f1)
                # print (countA)
                countB = len(f2)
                # print (countB)
                if countA != countB:
                    print(filename + '行数不相等！')
                    mylog(filename + '行数不相等！')
                #开始替换含关键词的行数
                Exist_lineA = []
                Exist_lineB = []
                # print(filename)
                for i in range(countA):
                    if (f1[i].find("//") == -1) and regex.findall(f1[i]) != []:
                        # print(f1[i])
                        Exist_lineA.append(i)
                for j in range(countB):
                    if (f2[j].find("//") == -1) and regex.findall(f2[j]) != []:
                        # print(f2[j])
                        Exist_lineB.append(j)
                # for i in range(countA):
                #     if (f1[i].find("//") == -1) and ((f1[i].find("SYS") != -1) or (f1[i].find("sys") != -1) or (f1[i].find("SEL") != -1) or (f1[i].find("SET_NAME") != -1) or (f1[i].find("MSG_EX") != -1) or (f1[i].find("msg") != -1)):
                #         # print(f1[i])
                #         Exist_lineA.append(i)
                # for j in range(countB):
                #     if (f2[j].find("//") == -1) and ((f2[j].find("SYS") != -1) or (f2[j].find("sys") != -1) or (f2[j].find("SEL") != -1) or (f2[j].find("SET_NAME") != -1) or (f2[j].find("MSG_EX") != -1) or (f2[j].find("msg") != -1)):
                #         # print(f2[j])
                #         Exist_lineB.append(j)
                
                # print(len(Exist_lineA))
                # print(len(Exist_lineB))
                if len(Exist_lineA) == len(Exist_lineB):
                    # 执行替换
                    # 指针回到开始并清空目标文件
                    F2file.seek(0)
                    F2file.truncate()
                    #  替换list对应行数
                    for k in range(len(Exist_lineA)):
                        f2[Exist_lineB[k]] = '	' + f1 [Exist_lineA[k]]
                        # print(f2[Exist_lineB[k]])
                    F2file.writelines(f2)
                                    
                else:
                    print(filename + "不同的符合条件行数！")
                    mylog(filename + "不同的符合条件行数！")
                    mylog(str(Exist_lineA))
                    mylog(str(Exist_lineB))
                    # os.system('pause') 
                F1file.close()
                F2file.close()
            except Exception as err:
                continue    
    
    
    # print (foldname.group())
    # print (filename)

if __name__== '__main__':
    myExchage()
    os.system('pause') 