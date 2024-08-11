#Dictionary

player = {
  'name': 'james',
  'age':20,
  'alive':True,
  'fav_food':["🥭", "🍎", "🌸", "🍺"]
}

print("1. Name:", player.get("name"))
print("2. Age:", player.get("age"))
print("3. Food:", player.get("fav_food"))
print("4. Food:", ", ".join(player.get("fav_food")))
print("4. Food:","/ ".join(player.get("fav_food")))
print("4. Food:","🥂".join(player.get("fav_food")))

player['fav_food'].append("🍉")
player['fav_food'].append("🐯")
print(player.get('fav_food'))
print(player.get("fav_food"))
print(player['fav_food'])
print(player["fav_food"])

print("Hello")
print('Hello')

print(player.get('fav_food')[0])
print(player.get('fav_food')[1])
print(player.get('fav_food')[2])
print(player.get('fav_food')[3])
print(player.get('fav_food')[4])
print(player.get('fav_food')[5])
print(player.get('fav_food')[-1])
print(player.get('fav_food')[-2])
print(player.get('fav_food')[-3])

#----------------
"""
#Tuple

days_tuple = ("Mon", "Tus", "Wed", "Thur", "Fri")
days_list = ["Mon", "Tus", "Wed", "Thur", "Fri"]

print(days_tuple[-3])

"""
#----------------
"""
#List
days_of_week = ["Mon","Tus","Wed", "Thur", "Fri"]

print(days_of_week)
print(days_of_week.count("Tus"))
days_of_week.reverse()
print(days_of_week)
days_of_week.append("Sat")
print(days_of_week)
days_of_week.append("Sun")
print(days_of_week)
"""
#----------------
"""
name = "david "
print(name.capitalize())
print(name.upper())
print(name.replace(" ","🍀"))
print(name.capitalize().replace(" ","🍀"))
"""
#----------------
"""from random import randint

print("Welcome to PYPY Casino!")

pc_choice = randint(1, 100)

playing = True

while playing:
  user_choice = int(input("choose number(1 ~ 100)"))
  if user_choice == pc_choice:
    print(f"You Choos {user_choice}! You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")
"""
#----------------
"""
distance = 0 

while distance <= 20:
  print(f"I'm running {distance} Km")
  distance = distance + 1
"""
#----------------
"""
#age = int(input("How old are you?"))

#if age < 18:
#  print("You can't drink")
#elif age > 18 and age < 35:
#  print("How about beer?")
#else:
#  print("Go ahead")
#print("age:", age)
#print(type(age))
"""

#----------------
"""
#def make_juice(fruit):
#  return f"{fruit}+🥤"

#def add_ice(juice):
#  return f"{juice}+🧊"

#def add_suger(iced_juice):
#  return f"{iced_juice}+🍬"

#fruit = ""
#print(fruit)
#juice = make_juice(fruit="💧💧💧")
#print(juice)
#iced_juice = add_ice(juice)
#print(iced_juice)
#perfect_juice = add_suger(iced_juice)
#print(perfect_juice)
"""

#----------------
"""
#def tax_calc(money):
#  return money * 0.35

#def pay_tax(tax):
#  print("Tnank you for paying", tax)

#pay_tax(tax_calc(100))
"""

#----------------
"""
#def plus(a=0, b=0):
#  print(a + b)

#def minus(a=0, b=0):
#  print(a - b)

#def multiple(a=0, b=1):
#  print(a * b)

#def divided(a=0, b=1):
#  print(a / b)

#def remainder(a=1, b=1):
#  print(a % b)

#def power(a=0, b=0):
#  print(a ** b)

#plus(3)
#minus(3)
#multiple(3)
#divided(3)
#remainder(3)
#power(3)
"""

#-----------
"""
#def say_hello(user_name="anonymus", user_age="??"):
#  print("helo", user_name, "how are you?", "you #are", user_age, "years old")

#say_hello("David", 18)
#say_hello()
#def say_bye():
#  print("Bye bye")

#say_bye()
#say_hello()
"""
