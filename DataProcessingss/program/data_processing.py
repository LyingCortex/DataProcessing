# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os, re


const1 = 1.013
const2 = 1.02


path = 'D:\Data\shuju'
files = os.listdir(path)


save_dir1 = 'D:\Data\const1.013'
if not os.path.exists(save_dir1):
    os.mkdir(save_dir1)


save_dir2 = 'D:\Data\const1.02'
if not os.path.exists(save_dir2):
    os.mkdir(save_dir2)

#save_dir2 = 'D:\Data\AfterProcess\const1.02'
#os.mkdir(save_dir2)
#print files
N = len(files)

for i in range(N):
    new_path = path + '\\' + files[i]
    #print new_path
    save_path1 = save_dir1 + '\\' + files[i]
    save_path2 = save_dir2 + '\\' + files[i]
    if os.path.isfile(save_path1):
        os.remove(save_path1)
    if os.path.isfile(save_path2):
        os.remove(save_path2)
    
    f = file(new_path,'r')
    rePattern = re.compile('\d.\d\d\n$')
    fout1 = file(save_path1,'w')
    fout2 = file(save_path2,'w')
    #column = []
    for line in f.readlines():
        row = line.split()
        #print line.split(' ')
        fout1.writelines(rePattern.sub(str('%.2f'%(float(row[-1])/const1))+'\n', line))
        fout2.writelines(rePattern.sub(str('%.2f'%(float(row[-1])/const2))+'\n', line))
        
        
    f.close()
    fout1.close()
    fout2.close()
        
        


   
    
    
        















 

