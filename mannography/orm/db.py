from os.path import exists, join
from .orm import *

import numpy as np
import sqlite3
import io


def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())


def convert_array(data):
    out = io.BytesIO(data)
    out.seek(0)
    return np.load(out)


class ContextDB(Context):
    def __init__(self):
        # convert np.array to txt when insert
        sqlite3.register_adapter(np.ndarray, adapt_array)

        # convert txt to np_array when selecting
        sqlite3.register_converter("array", convert_array)

        db_file = 'dataset.db'
        db_exists = exists(db_file)
        self.conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
        self.c = self.conn.cursor()

        if not db_exists:
            self.create_tables()

    def create_tables(self):
        # Create table
        self.c.execute('''CREATE TABLE normals
                    (img array, type text)''')

        self.c.execute('''CREATE TABLE benign_without_callbacks
                    (img array, type text)''')

        self.c.execute('''CREATE TABLE cancers
                    (img array, type text)''')

        self.c.execute('''CREATE TABLE benigns
                    (img array, type text)''')

    def insert(self, value, class_: int, diagnostic):
        '''
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
        '''
        print('--------------------------------------------' + diagnostic)
        query = 'INSERT INTO %s (img, type) VALUES (?,?)' % (diagnostic)
        self.c.execute(query, (value, TABLE[class_]))

    def select(self, class_: int, diagnostic: str):
        '''
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
        '''
        query = 'SELECT img FROM %s WHERE type= "%s"' % (diagnostic, TABLE[class_])
        print(query)
        self.c.execute(query)
        return self.c.fetchall()

    def commit(self):
        '''
            Save (commit) the changes
        '''
        self.conn.commit()

    def close(self):
        '''
         We can also close the connection if we are done with it.
         Just be sure any changes have been committed or they will be lost.
        '''
        self.conn.close()