import time
import sys
class Prints(object):
	def __init__(self,line):
		self.line = line

	def delay_print(self):
		for c in self.line:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.01)
	def slow_print(self):
		for c in self.line:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.05)
	def speedy_print(self):
		for c in self.line:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(.001)
	def insanelyfast_print(self):
		for c in self.line:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(.0001)
class Human(object):
  def __init__(self,name,hp,level,iq,strength,charisma):
    self.name = name
    self.hp = hp
    self.level = 1
    self.iq = iq
    self.strength = strength
    self.charisma = charisma
  def levelup(self):
    self.level += 1
    if self.level == 2:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 3:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 4:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 5:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 6:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 7:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 8:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 9:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 10:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 11:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 12:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 13:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    elif self.level == 14:
      self.hp = self.hp
      self.iq = self.iq
      self.strength = self.strength
      self.charisma = self.charisma
    else:
      return
  def damage(self,dmg):
    self.hp = self.hp - dmg
    return self.hp
  def description(self):
    return ("Name: {}\n HP: {}\nLevel: {}\nIQ: {}\nSTR: {}\nCHA: {}\n".format(self.name,self.hp, self.level,self.iq,self.strength,self.charisma))
