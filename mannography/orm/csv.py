from .orm import *
import os
import csv

class ContextCSV(Context):

    def __init__(self):
        self.db = open('train/label.csv', 'w')
        writer = csv.DictWriter(self.db, fieldnames=['File Name', 'Label'])
        writer.writeheader()

    def insert(self, value, class_: int, diagnostic):
        '''
        aqui poner las cosas en el csv respetando la configuracion de auto keras y la de la estructura de mannography
        :param value:
        :param class_:
        :param diagnostic:
        :return:
        '''
        pass
        # for current_class in class_dirs:
        #     for image in os.listdir(os.path.join(train_dir, current_class)):
        #         writer.writerow({'File Name': str(image), 'Label': label})
        #     label += 1

    def close_db(self):
        self.db.close()