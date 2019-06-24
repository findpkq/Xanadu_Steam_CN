
import re
import tkinter.filedialog
import tkinter.messagebox
import os,shutil,re
from tkinter import * 
from shutil import copyfile

# https://blog.csdn.net/lishenluo/article/details/79244257
# tkinter.messagebox.showinfo("Demo","info test")
# mainloop()

# def readFilename(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         return files,dirs,root

def findstring(pathfile):
    fp = open(pathfile, "r")
    strr = fp.read()
    if(strr.find("SYS") != -1) or (strr.find("sys") != -1) or (strr.find("SEL") != -1) or (strr.find("SET_NAME") != -1) or (strr.find("MSG") != -1) or (strr.find("msg") != -1) :
        # print("here?")
        fp.close
        return True
    return False 




def mycopy(filename,rawfile_path, target_dir):
    mydir = 'F:/copy/new_En_Exist/'
    # print(os.path.exists(mydir+target_dir))
    if (os.path.exists(mydir+target_dir)):
        print(target_dir+' exist!')
    else:
        os.makedirs(mydir+target_dir)
    shutil.copy(rawfile_path, mydir+target_dir+'/'+filename)


def myfind(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for ii in files:
            try:
                full_path = root+"\\"+ii
                if(findstring(full_path)):
                    # print (ii)
                    # print (root)
                    dirname = re.search('(?<=\\\\).*',root)
                    # print (dirname.group())
                    mycopy(ii,full_path,dirname.group())
                    # shutil.copy(full_path, 'F:/copy/'+dirname+'//'+ii)
            except Exception as err:
                continue

if __name__== '__main__':
    file_path = tkinter.filedialog.askdirectory()
    myfind(file_path)
    os.system('pause') 
