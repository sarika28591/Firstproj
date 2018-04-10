import random

class Enemy:
    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy(60 , 80)
enemy1.getAtk()

enemy2 = Enemy(20 ,90)
enemy2.getAtk()


class Fruits:
    def __init__(self , fruit1 , fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    def my_function(self):
        print(self.fruit1)
        print(self.fruit2)


object1 = Fruits("apple" , "banana")
object1.my_function()

object2 = Fruits("apple" , "banana")
object2.my_function()


