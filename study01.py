#선수 / 팀, 명단 추가, 제거 / XP 합산관련 -5강 완료!-

class Player: 
  def __init__(self, name, xp, team):
    self.name = name
    self.xp = xp
    self.team = team

  def introduce(self):
    print(f"Hey! I'm {self.name} in the {self.team}Team / XP:{self.xp}")

class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def show_players(self, exclude_player):
    print(f"\n{self.team_name} 팀 선수 명단:")
    total_xp = 0
    for player in self.players:
      if player.name != exclude_player:
        player.introduce()
        total_xp += player.xp
      else:
        total_xp += player.xp
    print(f"{self.team_name} 팀의 총 XP:{total_xp}")
    if exclude_player:
      print(f"*다음 선수는 명단에서 제외되었으나, 팀 XP에는 포함됨 :{exclude_player}")

  def add_player(self, name, xp):
    new_player = Player(name, xp, self.team_name)
    self.players.append(new_player)
    
t1 = Team("Time")
t1.add_player("손오공", 999)
t1.add_player("잔다르크", 900)
t1.add_player("그루트", 650)
t1.add_player("루시퍼", 999)

t2 = Team("Space")
t2.add_player("루피", 999)
t2.add_player("쵸파",1000)
t2.add_player("아이언맨",870)
t2.add_player("토르", 980)

t1.show_players("그루트")
t2.show_players("아이언맨")


#Player
"""
class Player: 
  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hey! I'm {self.name} in the {self.team}Team / XP:{self.xp}")

class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def show_players(self):
    for player in self.players:
      player.introduce()
  
  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)
    
t1 = Team("Time")
t1.add_player("David")
t2 = Team("Space")
t2.add_player("Ducachi")

t1.show_players()
t2.show_players()
"""

"""
#Class & Inheritance
class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("ZZZZ.....")
    
class guard(Dog):

  def __init__(self, name, breed):
    super().__init__(name, breed, 5,)
    self.agrrasive = True

  def BARK(self):
    print("WOOF WOOF!")
  
class puppy(Dog):
  def __init__(self, name, breed):
    super().__init__(name, breed, 0.1,)
    self.kindness = True
    
  def bark(self):
    print("woof woof~")

coco = puppy("coco", "pome")
chico = guard("chico","chihuahua")

coco.bark()
coco.sleep()

chico.BARK()
chico.sleep()
"""

#Class
"""
class puppy:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def __str__(self):
    return f"{self.name} is a {self.breed} and is {self.age} years old"
  def bark(self):
    print("WOOF WOOF!")
  def introduce(self):
    self.bark()
    print(f"Hey My name is {self.name}, {self.age} years old, and {self.breed} ")

coco = puppy(name="coco", age="1", breed="golden retriever")
cico = puppy("nico", "2", "chihuahua")


print(coco)
coco.bark()
print(nico)
coco.bark()

coco.introduce()
cico.introduce()
"""
#Class
"""
class puppy:
  def __init__(self):
    self.name = "coco"
    self.age = "5"
    self.breed = "golden retriever"
    self.color = "golden"

coco = puppy()

print(
  coco.name,
  coco.age,
  coco.breed,
  coco.color
)
"""

# For Loop / URL formatting / Status Codes
"""
from requests import Response, get #패키지 설치를 통해서 가져올 수 있음

websites = (
  "google.com", 
  "httpstat.us/101", 
  "httpstat.us/200",
  "httpstat.us/308",
  "httpstat.us/400"
  "httpstat.us/561"
)

result = {}

for website in websites:
  if not website.startswith ("https://"):
    website = f"https://{website}"
    response = get(website)    
  if response.status_code >= 100 and response.status_code < 200:
    result[website] = "1XX error"
  elif response.status_code >= 200 and response.status_code < 300:
    result[website] = "OK"
  elif response.status_code >= 300 and response.status_code < 400:
    result[website] = "3XX error"
  elif response.status_code >= 400 and response.status_code < 500:
    result[website] = "4XX error" 
  elif response.status_code >= 500 and response.status_code <= 561:
    result[website] = "5XX error"
  else:
    result[website] = "Failed"
    
print(result)
"""

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
