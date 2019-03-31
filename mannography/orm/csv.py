from .orm import *
import os
import csv
import cv2

class ContextCSV(Context):

    def __init__(self):
        self.path = 'dataset/'
        self.db = open(self.path+'label.csv', 'x')
        self.writer = csv.DictWriter(self.db, fieldnames=['File Name', 'Label'])
        self.writer.writeheader()
        self.img_name = 0

    def insert(self, value, class_: int, diagnostic):
        '''
        Creo que lo mejor para esto es hacer un csv para cada class(posicion de la mama)
         class_ :
            0 - right_mlo
            1 - right_cc
            2 - left_mlo
            3 - left_cc

            diagnostic:
            * normals
            * benign_without_callbacks
            * cancers
            * benigns

        :param value:
        :param class_:
        :param diagnostic:
        :return:
        '''

        cv2.imwrite(self.path+'/'+str(self.img_name)+'.png', value)
        self.writer.writerow({'File Name': str(self.img_name), 'Label': diagnostic})
        self.img_name += 1


    def close_db(self):
        self.db.close()