#!/usr/bin/env python

'''
Follwoing program gives the examples of accessing Files

Author  :  Nallaparaju Krishna

Date :  06-12-2020

'''

#Opening the File

File_Handle = open("README.md", encoding='utf-8')   #Open File in current directory

for i in File_Handle:
    print(i)

File_Handle.close()


