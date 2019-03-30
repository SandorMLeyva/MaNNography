
import cv2
from matplotlib import pyplot as plt


class ResizeImg:
    def __init__(self, scaleX = 0.1, scaleY = 0.1):
        self.scaleX = scaleX
        self.scaleY = scaleY  

    def load(self, path):
        self.image = cv2.imread(path,0)
        self.h = len(self.image)
        self.w = len(self.image[0])

    def crop(self, h_offset = 0, w_offset = 500):
        # TODO: tener en cuenta que si es izquierda o derecha hay q ver de donde se recorta
        self.crop_img = self.image[h_offset:self.h, w_offset:self.w]
        a = "CROP: --> from: %s X %s  to %s X %s"%(self.h,self.w,len(self.crop_img),len(self.crop_img[1]))
        print(a)

    def scale(self):
        self.crop_img = cv2.resize(self.crop_img, None, fx= self.scaleX, fy= self.scaleY, interpolation= cv2.INTER_LINEAR)
        a = "SCALE: -->  %s X %s"%(len(self.crop_img),len(self.crop_img[1]))
        print(a)

    def save_img(self, path):
        cv2.imwrite(path, self.crop_img)

    @property
    def get_np_array(self):
        return self.crop_img

    def resize(self, path, position = 0):
        '''
        position: 
            0 rigth
            1 left
        '''
        self.load(path)
        if position == 1:
            self.crop(h_offset= 500, w_offset= 0)
        else:    
            self.crop()
        self.scale()
        return self.crop_img
