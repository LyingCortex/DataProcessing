# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import decimal
decimal.getcontext().prec = 3

const1 = 1.013
const2 = 1.02


path = 'D:\Data\liuyangshuju'
files = os.listdir(path)


save_dir1 = 'D:\Data\const1.013'
os.mkdir(save_dir1)


save_dir2 = 'D:\Data\const1.02'
os.mkdir(save_dir2)

#save_dir2 = 'D:\Data\AfterProcess\const1.02'
#os.mkdir(save_dir2)
#print files
N = len(files)

for i in range(N):
    new_path = path + '\\' + files[i]
    print new_path
    save_path1 = save_dir1 + '\\' + files[i]
    save_path2 = save_dir2 + '\\' + files[i]
    f = file(new_path,'r')
    fout1 = file(save_path1,'w')
    fout2 = file(save_path2,'w')
    #column = []
    for line in f.readlines():
        row = line.split()
        fout1.writelines('       '.join(row[0:-1]))
        fout1.write('       '+ str(float(decimal.Decimal(row[-1])/decimal.Decimal(const1)))+'\n')
        fout2.writelines('       '.join(row[0:-1]))
        fout2.write('       '+ str(float(decimal.Decimal(row[-1])/decimal.Decimal(const2)))+'\n')
        
    f.close()
    fout.close()
        
       

   
    
    
        















 

