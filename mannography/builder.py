#!/usr/bin/env python
# coding: utf-8

from .orm import Context
from .resizer import ResizeImg
import numpy as np
import sys
import os


class Builder:
    def __init__(self):
        self.path = 'mamografias'
        self.clasifications = ['normals', 'benign_without_callbacks', 'cancers', 'benigns']
        self.resizer = ResizeImg()
        self.context = Context()


    def classificate_file(self, path: str, folder):
        if os.path.isfile(path) and os.path.split(path)[1].split('.')[-1] == "png":
            # aqui se hace el analisis con la imagen y luego se guarda en la bd
            if path.count('RIGHT_MLO') == 1:
                img = self.resizer.resize(path)
                self.context.insert(img,0,folder)
            if path.count('RIGHT_CC') == 1:
                img = self.resizer.resize(path)
                self.context.insert(img,1, folder)
            if path.count('LEFT_MLO') == 1:
                img = self.resizer.resize(path, position=1)
                self.context.insert(img,2, folder)
            if path.count('LEFT_CC') == 1:
                img = self.resizer.resize(path, position=1)
                self.context.insert(img,3, folder)


    def find_file(self, path: str, class_: str = 'none'):
        """
        :params: `path` a string representing the path to the dataset.
        """
        for folder_path, folder in [(os.path.join(path,name), name) for name in os.listdir(path)]:
            if os.path.isdir(folder_path):
                if folder in self.clasifications:
                    self.find_file(folder_path, folder)
                else:
                    self.find_file(folder_path, class_)
            else:
                self.classificate_file(folder_path, class_)


# def main():
#     if sys.argv.count('createdb') == 1:
#         db.create_tables()
#         db.commit()           
#     elif sys.argv.count('get') == 1:
#         print(sys.argv)
#         class_  = int(sys.argv[2])
#         diagnostic = sys.argv[3]
#         db.select(class_,diagnostic)
#         print(db.select(class_,diagnostic))
#     elif sys.argv.count('help') == 1:
#         print('''
#             createdb
#             get [class] [diagnostic]  
#                 class:
#                 0 - right_mlo
#                 1 - right_cc
#                 2 - left_mlo
#                 3 - left_cc

#                 diagnostic:
#                 * normals
#                 * benign_without_callbacks
#                 * cancers
#                 * benigns
#         ''')
#     else:
#         if len(sys.argv)>1:
#             path = sys.argv[1]
#         find_file(path)
#         db.commit()
#     db.close()

# if __name__ == '__main__':
#     main()
