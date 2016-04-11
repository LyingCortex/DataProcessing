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
const = [1.013, 1.02]

path = 'D:\Data\liuyangshuju'
files = os.listdir(path)

save_dir= 'D:\Data\AfterProcess'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)




#save_dir2 = 'D:\Data\AfterProcess\const1.02'
#os.mkdir(save_dir2)
#print files
N = len(files)

for i in range(N):
    new_path = path + '\\' + files[i]
    #print new_path
    
    f = file(new_path,'r')
    save_path = []
    fout=[]
    for ii in range(len(const)):
        if not os.path.exists(save_dir + '\\const' + str(const[ii])):
            os.mkdir(save_dir + '\\const' + str(const[ii]))
        save_path.append(save_dir + '\\const' + str(const[ii]) + '\\' + files[i])
        if os.path.isfile(save_path[ii]):
            os.remove(save_path[ii])
        fout.append(file(save_path[ii],'w'))
        for line in f:
            row =line.replace('\n','').split(' ')
            fout[ii].writelines(''.join(row[0:-1]))
            fout[ii].write(str(float(decimal.Decimal(row[-1])/decimal.Decimal(const[ii])))+'\n')
        fout[ii].close()
       
       
    f.close()
#    fout.close()
        
       

   
    
    
        















 

