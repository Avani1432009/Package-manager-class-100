#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lenovo
#
# Created:     22-12-2021
# Copyright:   (c) lenovo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

#os.mkdir("/backupFiles/")
print(os.getcwd())
#os.getcwd()
path = ("C:/backupFiles/crow.png")

isExist = os.path.exists(path)
print(isExist)
root_ext = os.path.splitext(path)
print("root part ",root_ext[0])
print("ext part ",root_ext[1],"\n")

os.listdir()

import shutil

#source = "C:/backupFiles/crow.png"
#destination = "C:/backupFiles/crow1.png"
#dest = shutil.copy(source,destination)

#source = "C:/dustbin/notes5.txt"
#destination = "C:/backupFiles/"
#dest = shutil.move(source,destination)

class Car(object):

 def __init__(self,model,color,company,speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self. model = model

 def start(self):
    print('started')

 def stop(self):
    print('stopped')

 def accelarate(self):
    print('accelarating...')
    'accelarator functionality here'
 def change_gear(self,gear_type):
    print('gear changed')
    'gear related functionality here'

audi = Car('A6','red','audi',80)

print(audi.start())
print(audi.color)
print(audi.stop())
print(audi.accelarate())
