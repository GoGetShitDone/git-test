class Dog:

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Dog: {self.name}"


jia = Dog("jia")
digo = Dog("digo")
print(jia)
print(dir(jia))

# print(digo)

# class Human:

#   def __init__(self, name):
#     self.name = name

#   def say_hello(self):
#     print(f"Hello I'm {self.name}")

# class Player(Human):

#   def __init__(self, name, xp):
#     super().__init__(name)
#     self.xp = xp
#     print(f"XP: {self.xp}")

# class Fan(Human):

#   def __init__(self, name, fav_team):
#     super().__init__(name)
#     self.fav_team = fav_team
#     print(f"I'm big fan of {self.fav_team}")

# cico_human = Human("Cico")
# cico_human.say_hello()
# nico_fan = Fan("Nico", "X")
