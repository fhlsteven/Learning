# -*- coding: utf-8 -*-
import os

DWONLOAD_DATA = []

def check_repeat():
    all_data = []
    for x in DWONLOAD_DATA:
        all_data.append(x.split('_'))

    duplicates = []
    tempid=[]
    for x in all_data:
        if x[1] in tempid:
            duplicates.append(x)
        else:
            tempid.append(x[1])
    print(duplicates)

if __name__ == '__main__':
    DWONLOAD_DATA = os.listdir('./file')
    check_repeat()