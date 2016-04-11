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

#print files
N = len(files)
new_path = []
for i in range(N):
    new_path.append(path + '\\' + files[i])
print new_path



f = open(path)
column = []

for line in f:
    ll = line.replace('\n','').split(' ')
    column.append(eval(ll[-1]))

print column

new_column =[float(decimal.Decimal(x)/decimal.Decimal(const1)) for x in  column]
print new_column




 

