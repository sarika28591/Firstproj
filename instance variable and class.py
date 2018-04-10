import random

class Enemy:
    hp = 200

    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("the atk is" , self.atkl)

    def gethp(self):
        print("Hp is" , self.hp)


enemy1 = Enemy(60 , 80)
enemy1.getAtk()
enemy1.gethp()

enemy2 = Enemy(20 ,90)
enemy2.getAtk()
enemy2.gethp()



# example
class Fruits:
    King = ("Mango")

    def __init__(self , fruit1 , fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    def my_function(self):
        print("Fruit name is" , self.fruit1)
        print("Fruit name is" , self.fruit2)

    def newking(self):
        print("But the main fruit is" , self.King)


object1 = Fruits("apple" , "banana")
object1.my_function()
object1.newking()

object2 = Fruits("watermelon" , "grapes")
object2.my_function()
object2.newking()