import random

class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()


'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp == 30:
        print("you have low health")
        break
'''
import random

class Fruits:
     fruit1 = ("apple")
     fruit2 = ("banana")

     def my_function(self):
         print(self.fruit1)
         print(self.fruit2)

object1 = Fruits()
object1.my_function()

object2 = Fruits()
object2.my_function()


import random

class Games:
    Game1 = [1 ,2 ,3 ,4][0]
    Game2 = ("cricket")

    def my_game(self):
        print(self.Game1)

object1 = Games()
object1.my_game()

