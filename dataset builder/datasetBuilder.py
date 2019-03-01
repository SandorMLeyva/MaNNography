#!/usr/bin/env python
# coding: utf-8

from db_manage import dbManage
from resize import ResizeImg
import numpy as np
import sys
import os


FOLDER = 'mamografias'
PATH = '.'
CLASIFICATIONS = ['normals', 'benign_without_callbacks', 'cancers', 'benigns']
path = os.path.join(PATH,FOLDER)
resize_img = ResizeImg()
db = dbManage()


def clasificate_file(path: str, folder):
    if os.path.isfile(path) and os.path.split(path)[1].split('.')[-1] == "png":
        # aqui se hace el analisis con la imagen y luego se guarda en la bd
        if path.count('RIGHT_MLO') == 1:
            img = resize_img.resize(path)
            db.insert(img,0,folder)
        if path.count('RIGHT_CC') == 1:
            img = resize_img.resize(path)
            db.insert(img,1, folder)
        if path.count('LEFT_MLO') == 1:
            img = resize_img.resize(path)
            db.insert(img,2, folder)
        if path.count('LEFT_CC') == 1:
            img = resize_img.resize(path)
            db.insert(img,3, folder)


def find_file(path:str, class_:str = 'none'):   
    for folder_path, folder in [(os.path.join(path,name), name) for name in os.listdir(path)]:
        if os.path.isdir(folder_path):
            if folder in CLASIFICATIONS:
                find_file(folder_path, folder)
            else:
                find_file(folder_path, class_)
        else:
            clasificate_file(folder_path, class_)


def main():
    if sys.argv.count('createdb') == 1:
        db.create_tables()
        db.commit()           
    elif sys.argv.count('get') == 1:
        print(sys.argv)
        class_  = int(sys.argv[2])
        diagnostic = sys.argv[3]
        db.select(class_,diagnostic)
        print(db.select(class_,diagnostic))
    elif sys.argv.count('help') == 1:
        print('''
            createdb
            get [class] [diagnostic]  
                class:
                0 - right_mlo
                1 - right_cc
                2 - left_mlo
                3 - left_cc

                diagnostic:
                * normals
                * benign_without_callbacks
                * cancers
                * benigns
        ''')
    else:
        if len(sys.argv)>1:
            path = sys.argv[1]
        find_file(path)
        db.commit()
    db.close()

if __name__ == '__main__':
    main()
