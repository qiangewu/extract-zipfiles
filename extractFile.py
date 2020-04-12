import zipfile
import os

def extract(password,fileName):
    try:
        if os.path.isdir(fileName):
            fileDir = fileName
        else:
            fileDir = os.path.dirname(fileName)
        print('Start extract file: {},use psw: {},path: {}'.format(fileName,password,fileDir))
        zfile = zipfile.ZipFile(fileName,'r')
        # zfile.extractall(pwd=bytes(password,"utf-8"))
        zfile.extractall(path=fileDir,pwd=str(password).encode('ascii'))
        # for file in zfile.namelist():
        #     # zfile.extract(file,str(password))
        #     zfile.extract(file,'','123')
    except Exception as e:
        print(e)
        return False


    else:
        print('解压完成')
        return True
    finally:
        print('end\n')

def trim(s):
    if len(s)==0:
        return ''
    if s[:1]==' ':
        return trim(s[1:])
    elif s[-1:]=='' or s[-1:]=='\n':
        return trim(s[:-1])
    else:
        return s

def listPasswords(fileName):
    j =  0
    keylist = []
    f = open(fileName,'r',encoding='utf-8')
    list = f.readlines()
    for i in range(0,len(list)):
        if(list[i]!='\n'):
            keylist.append(trim(list[i]))
            j += 1
    return keylist

def listDirFiles(dir):
    fileList = []
    if not os.path.exists(dir):
        print('当前路径不存在')
        return -1
    if os.path.isfile(dir):
        if dir.endswith('.zip'):
            fileList.append(dir)
    else:
        for root,dirs,files in os.walk(dir,True):
            for dir in dirs:
                print('dir: {}'.format(dir))
            for file in files:
                if file.endswith('.zip'):
                    fileList.append(os.path.join(root,file))
                    print('file: {}'.format(os.path.join(root,file)))
    return fileList

if __name__ == "__main__":
    keys = listPasswords(r'C:\Users\Touch Spring\Desktop\key.txt')
    fileDir = r'C:\Users\Touch Spring\Desktop\new'
    fileList = listDirFiles(fileDir)
    for file in fileList:
        for key in keys:
            if extract(key,file):
                break
            else:
                continue