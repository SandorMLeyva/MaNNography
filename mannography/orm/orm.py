CLASIFICATIONS = ['normals', 'benign_without_callbacks', 'cancers', 'benigns']
TABLE = ['right_mlo', 'right_cc', 'left_mlo', 'left_cc']

class Context:

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


