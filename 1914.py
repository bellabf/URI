#!/usr/bin/env python

qt = int(input())

for i in range(qt):

    dataname = input().split()

    datanum = []
    
    for i in input().split(): datanum.append(int(i))

    if( (datanum[0]+datanum[1]) % 2 == 0):
        
        pos = dataname.index('PAR')

    else: 
    
        pos = dataname.index('IMPAR')
    
    print(dataname[pos-1])
